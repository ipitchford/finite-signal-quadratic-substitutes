"""Release regression suite: exact checks remain active in optimized Python."""
from fractions import Fraction as Q
import json
import random
from exact import model, means, margins, residual, reverse, witness, direct_gap
from test_sharp_coefficient import coefficient, require, variance, main as sharp_tests


def main():
    rng = random.Random(15102026)
    counts = dict(directions=0,negative_witnesses=0,positive_posteriors=0,
                  sparse_edges=0,invalid_inputs=0,negative_controls=0)
    for trial in range(300):
        n,m = 2+trial%4,2+(trial//4)%4
        z = [[rng.randrange(1,10) for _ in range(m)] for _ in range(n)]
        r = [[Q(a,sum(row)) for a in row] for row in z]
        v = [[Q(rng.randrange(11),10) for _ in range(m)] for _ in range(n)]
        pi = [Q(1,n)]*n
        for rr,vv,pp in [(r,v,pi), reverse(r,v,pi)]:
            counts['directions'] += 1
            w = witness(rr,vv,pp)
            if w is not None:
                kernel=w['kernel']
                require(all(sum(row)==1 and min(row)>=0 for row in kernel),'Bad witness channel')
                g=direct_gap(rr,vv,pp,kernel)
                require(g<0 and g==w['direct_gap'],'Bad direct gap')
                require(g==w['report_mass']*residual(rr,vv,w['posterior']),'Bad posterior identity')
                counts['negative_witnesses']+=1
            else:
                require(min(a for row in margins(rr,vv) for a in row)>=0,'Missed failure')
                for _ in range(10):
                    z=[rng.randrange(1,10) for _ in rr]
                    q=[Q(a,sum(z)) for a in z]
                    require(residual(rr,vv,q)>=0,'Positive test failed')
                    counts['positive_posteriors']+=1
    sr=[[Q(1,2),Q(1,2),0],[0,Q(1,2),Q(1,2)],[Q(1,2),0,Q(1,2)]]
    sv=[[0,0,0],[0,1,Q(1,2)],[1,0,Q(1,2)]]
    require(direct_gap(sr,sv,[Q(1,3)]*3,[[1]]*3)==Q(-1,24),'Sparse gap')
    for i,j in [(0,1),(0,2),(1,2)]:
        for k in range(1,20):
            q=[Q(0)]*3;q[i]=Q(k,20);q[j]=1-q[i]
            require(direct_gap(sr,sv,q,[[1]]*3)>=0,'Sparse edge')
            counts['sparse_edges']+=1
    for invalid in [([],[],[]), ([[1,0]],[[0,1]],[1]),
                    ([[0.5,0.5]],[[0,1]],[1]), ([[1]],[[0]],['1/2'])]:
        try:
            model(*invalid)
        except ValueError:
            counts['invalid_inputs']+=1
        else:
            raise RuntimeError('Invalid input accepted')
    # Deliberately false outputs must be rejected by the check primitive.
    for false_statement in [Q(-1,24)>=0, Q(2)<=Q(3,2), Q(100,289)==Q(1)]:
        try:
            require(false_statement,'Expected semantic negative control')
        except RuntimeError:
            counts['negative_controls']+=1
        else:
            raise RuntimeError('Corrupted claim accepted')
    print(json.dumps(counts,sort_keys=True))
    sharp_tests()


if __name__=='__main__':
    main()
