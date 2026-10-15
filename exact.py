"""Exact finite-signal criterion; scalar quadratic value, full signal support.

Input cells are conditional means v and conditional probabilities r, with prior pi.
This is a research prototype, not a claim of formal verification.
"""
from fractions import Fraction as Q
import json, random
from pathlib import Path

def model(r, v, pi):
    if not r or not r[0] or len(v)!=len(r) or len(pi)!=len(r):
        raise ValueError('Nonempty, matching dimensions required')
    if any(isinstance(z, float) for row in r+v for z in row) or any(isinstance(z,float) for z in pi):
        raise ValueError('Use integers or rational strings, never floats')
    r=[[Q(z) for z in row] for row in r]; v=[[Q(z) for z in row] for row in v]; pi=list(map(Q,pi))
    n=len(r); m=len(r[0])
    if not all(len(row)==m for row in r+v): raise ValueError('Ragged table')
    if not all(z>0 for row in r for z in row) or not all(sum(row)==1 for row in r):
        raise ValueError('Strictly positive stochastic rows required; sparse support is outside the theorem')
    if not all(z>0 for z in pi) or sum(pi)!=1: raise ValueError('Positive probability prior required')
    return r,v,pi

def means(r,v): return [sum(a*b for a,b in zip(ri,vi)) for ri,vi in zip(r,v)]
def margins(r,v):
    x=means(r,v)
    return [[(x[i]-x[j])**2-sum(r[i][b]*(v[i][b]-v[j][b])**2 for b in range(len(r[0]))) for j in range(len(r))] for i in range(len(r))]

def residual(r,v,q):
    x=means(r,v); p=[sum(q[i]*r[i][b] for i in range(len(r))) for b in range(len(r[0]))]
    return sum(q[i]*x[i]**2 for i in range(len(r)))-sum(q[i]*x[i] for i in range(len(r)))**2-sum(q[i]*r[i][b]*v[i][b]**2 for i in range(len(r)) for b in range(len(p)))+sum(sum(q[i]*r[i][b]*v[i][b] for i in range(len(r)))**2/p[b] for b in range(len(p)))

def direct_gap(r,v,pi,kernel):
    """Independently aggregate signal/report cells to calculate four scores."""
    n=len(r); m=len(r[0]); reports=len(kernel[0]); x=means(r,v)
    full=sum(pi[i]*r[i][b]*v[i][b]**2 for i in range(n) for b in range(m))-sum(pi[i]*x[i]**2 for i in range(n))
    partial=Q(0)
    for t in range(reports):
        weights=[sum(pi[i]*kernel[i][t]*r[i][b] for i in range(n)) for b in range(m)]
        numer=[sum(pi[i]*kernel[i][t]*r[i][b]*v[i][b] for i in range(n)) for b in range(m)]
        partial+=sum(a*a/w for a,w in zip(numer,weights) if w)
        if sum(weights): partial-=sum(numer)**2/sum(weights)
    return partial-full

def witness(r,v,pi):
    mm=margins(r,v); n=len(r)
    for i in range(n):
        for j in range(n):
            if mm[j][i]>=0: continue
            # At posterior (1-t)e_i+t e_j, H(0)=M_ji.
            eps=-mm[j][i]
            L=sum(r[i][b]*r[j][b]*(v[i][b]-v[j][b])**2*abs(r[i][b]-r[j][b])/min(r[i][b],r[j][b])**2 for b in range(len(r[0])))
            t=min(Q(1,2),eps/(2*L)) if L else Q(1,2)
            q=[Q(0)]*n; q[i]=1-t; q[j]=t
            alpha=min(pi[k]/q[k] for k in range(n) if q[k])/2
            kernel=[]
            for k in range(n):
                row=[alpha*q[k]/pi[k]]+[Q(0)]*n
                row[k+1]=1-row[0]; kernel.append(row)
            gap=direct_gap(r,v,pi,kernel)
            assert gap==alpha*residual(r,v,q)<0
            return dict(pair=[i,j],failed_margin_indices=[j,i],posterior=q,report_mass=alpha,kernel=kernel,direct_gap=gap)
    return None

def reverse(r,v,pi):
    p=[sum(pi[i]*r[i][b] for i in range(len(r))) for b in range(len(r[0]))]
    return [[pi[i]*r[i][b]/p[b] for i in range(len(r))] for b in range(len(p))],list(map(list,zip(*v))),p

def run():
    rng=random.Random(15102026); counts={'passing_directions':0,'negative_witnesses':0,'posterior_checks':0}
    good=model([['4/5','1/5'],['1/2','1/2'],['1/5','4/5']], [['0','3/10'],['1/10','4/10'],['1/5','1/2']],['1/3']*3)
    for a in range(31):
        for b in range(31-a):
            assert residual(*good[:2],[Q(a,30),Q(b,30),Q(30-a-b,30)])>=0
            counts['posterior_checks']+=1
    examples=[]
    for trial in range(300):
        n=2+trial%4; m=2+(trial//4)%4
        rows=[[rng.randrange(1,10) for _ in range(m)] for _ in range(n)]
        r=[[Q(z,sum(row)) for z in row] for row in rows]
        v=[[Q(rng.randrange(11),10) for _ in range(m)] for _ in range(n)]
        pi=[Q(1,n)]*n
        for rr,vv,pp in [(r,v,pi),reverse(r,v,pi)]:
            w=witness(rr,vv,pp)
            if w:
                counts['negative_witnesses']+=1
                if not examples: examples.append(dict(r=rr,v=vv,pi=pp,witness=w))
            else:
                counts['passing_directions']+=1
                for _ in range(10):
                    z=[rng.randrange(1,10) for _ in rr]; q=[Q(a,sum(z)) for a in z]
                    assert residual(rr,vv,q)>=0
                    counts['posterior_checks']+=1
    out=dict(seed=15102026,counts=counts,positive_example=dict(r=good[0],v=good[1],pi=good[2],margins=margins(*good[:2])),negative_examples=examples)
    Path(__file__).with_name('exact-results.json').write_text(json.dumps(out,default=str,indent=2)+'\n')
    print(json.dumps(counts))
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',help='JSON object with r, v, pi; integers and rational strings only')
    args=parser.parse_args()
    if not args.input: run()
    else:
        data=json.loads(Path(args.input).read_text()); original=model(data['r'],data['v'],data['pi'])
        result={}
        for name,(r,v,pi) in [('A',original),('B',reverse(*original))]:
            w=witness(r,v,pi)
            result[name]=dict(passes=w is None,margins=margins(r,v),witness=w)
        print(json.dumps(result,default=str,indent=2))
