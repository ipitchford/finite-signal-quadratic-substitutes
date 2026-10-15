"""Exact rational certificate verification for sparse scalar tables.

No numerical solver, universal proof claim, or complete rational search is implied.
"""
from fractions import Fraction as Q
import json
from exact import direct_gap


def rational(value):
    if isinstance(value, (float, bool)):
        raise ValueError('Exact integer or rational input required')
    return Q(value)


def sparse_model(r, v, pi):
    if not r or not r[0] or len(r) != len(v) or len(r) != len(pi):
        raise ValueError('Nonempty matching dimensions required')
    m = len(r[0])
    if any(len(row) != m for row in r + v):
        raise ValueError('Ragged input')
    r = [[rational(a) for a in row] for row in r]
    if any(min(row) < 0 or sum(row) != 1 for row in r):
        raise ValueError('Nonnegative stochastic rows required')
    # Null cells must not acquire semantic values from arbitrary placeholders.
    v = [[rational(v[i][b]) if r[i][b] else Q(0)
          for b in range(m)] for i in range(len(r))]
    pi = list(map(rational, pi))
    if min(pi) <= 0 or sum(pi) != 1:
        raise ValueError('Positive probability prior required')
    return r, v, pi


def moments(r, v, q):
    q = list(map(rational, q))
    if len(q) != len(r) or min(q) < 0 or sum(q) != 1:
        raise ValueError('Invalid posterior')
    x = [sum(a*b for a,b in zip(ri,vi)) for ri,vi in zip(r,v)]
    D = sum(a*b*b for a,b in zip(q,x)) - sum(a*b for a,b in zip(q,x))**2
    N = Q(0)
    for b in range(len(r[0])):
        p = sum(q[i]*r[i][b] for i in range(len(r)))
        if p:
            u = sum(q[i]*r[i][b]*v[i][b] for i in range(len(r)))
            N += sum(q[i]*r[i][b]*v[i][b]**2 for i in range(len(r))) - u*u/p
    return D,N


def verify_completion(r, v, C, knots):
    C = rational(C)
    if C < 0:
        raise ValueError('Negative coefficient')
    x = [sum(a*b for a,b in zip(ri,vi)) for ri,vi in zip(r,v)]
    parsed = {rational(t):list(map(rational,z)) for t,z in knots.items()}
    if set(parsed) != set(x):
        raise ValueError('Certificate must cover every distinct source mean')
    margins = []
    for t,z in parsed.items():
        if len(z) != len(r[0]):
            raise ValueError('Wrong completion dimension')
        for i in range(len(r)):
            margin = C*(x[i]-t)**2 - sum(r[i][b]*(v[i][b]-z[b])**2 for b in range(len(z)))
            if margin < 0:
                raise ValueError('False completion inequality')
            margins.append(margin)
    return margins


def violating_disclosure(r, v, pi, q):
    q = list(map(rational,q))
    D,N = moments(r,v,q)
    if D-N >= 0:
        raise ValueError('Posterior is not a strict substitute violation')
    alpha = min(p/a for p,a in zip(pi,q) if a)/2
    kernel = []
    for i in range(len(r)):
        row = [alpha*q[i]/pi[i]] + [Q(0)]*len(r)
        row[i+1] = 1-row[0]
        if min(row) < 0 or sum(row) != 1:
            raise ValueError('Invalid disclosure')
        kernel.append(row)
    gap = direct_gap(r,v,pi,kernel)
    if gap != alpha*(D-N) or gap >= 0:
        raise ValueError('Direct four-score check failed')
    return dict(posterior=q, mass=alpha, kernel=kernel, gap=gap)


def main():
    count = 0
    def check(ok):
        nonlocal count
        if not ok:
            raise RuntimeError('Exact extension check failed')
        count += 1
    r,v,pi = sparse_model([[Q(1,2),Q(1,2),0],[0,Q(1,2),Q(1,2)],
                           [Q(1,2),0,Q(1,2)]],
                          [[0,0,None],[None,1,Q(1,2)],[1,None,Q(1,2)]],[Q(1,3)]*3)
    check(min(verify_completion(r,v,Q(16,9),{Q(0):[0,0,Q(1,2)],Q(3,4):[1,1,Q(1,2)]})) == 0)
    D,N = moments(r,v,pi)
    check((D,N) == (Q(1,8),Q(1,6)))
    check(violating_disclosure(r,v,pi,pi)['gap'] == Q(-1,48))
    for k in [10,100,1000,10000]:
        q = [Q(1,k),Q(k-1,2*k),Q(k-1,2*k)]
        d,n = moments(r,v,q)
        check(n/d <= Q(16,9))
    check(Q(16,9)-n/d < Q(1,1000))
    last_edge_ratio = n/d
    # Same genuinely overlapping sparse support, now a strict substitute.
    rp,vp,pp = sparse_model(r,[[0,0,None],[None,Q(1,2),1],[Q(1,2),None,1]],pi)
    check(min(verify_completion(rp,vp,Q(4,9),
        {Q(0):[0,0,1],Q(3,4):[Q(1,2),Q(1,2),1]})) == 0)
    dp,np = moments(rp,vp,pp)
    check(np <= Q(4,9)*dp and dp > 0)
    # Equal means with a disagreement on an overlapping cell force infinity.
    ri,vi,pii = sparse_model([[Q(1,2),Q(1,2)]]*2,
                            [[0,1],[1,0]],[Q(1,2)]*2)
    di,ni = moments(ri,vi,pii)
    check(di == 0 and ni > 0)
    check(violating_disclosure(ri,vi,pii,pii)['gap'] < 0)
    # One distinct mean, compatible shared cell, and row-private coordinates.
    rc,vc,pc = sparse_model([[Q(1,2),Q(1,2),0],[Q(1,2),0,Q(1,2)]],
                            [[0,1,None],[0,None,1]],[Q(1,2)]*2)
    check([sum(a*b for a,b in zip(ri,vi)) for ri,vi in zip(rc,vc)] == [Q(1,2)]*2)
    check(verify_completion(rc,vc,0,{Q(1,2):[0,1,1]}) == [0,0])
    for qc in [[Q(1),Q(0)],[Q(0),Q(1)],[Q(1,2)]*2,[Q(1,3),Q(2,3)]]:
        check(moments(rc,vc,qc) == (0,0))
    check(direct_gap(rc,vc,pc,[[1],[1]]) == 0)
    try:
        verify_completion(rc,vc,0,{Q(1,2):[1,1,1]})
    except ValueError:
        check(True)
    else:
        raise RuntimeError('Corrupt compatible equal-mean certificate accepted')
    # Reject realistic certificate mutations, not merely false booleans.
    for C,knots in [(1,{Q(0):[0,0,Q(1,2)],Q(3,4):[1,1,Q(1,2)]}),
                    (Q(16,9),{Q(0):[0,0,Q(1,2)]}),
                    (Q(16,9),{Q(0):[1,0,Q(1,2)],Q(3,4):[1,1,Q(1,2)]})]:
        try:
            verify_completion(r,v,C,knots)
        except ValueError:
            check(True)
        else:
            raise RuntimeError('Corrupt certificate accepted')
    # Every source is already revealed by B: sparse zero coefficient.
    rr,vv,pp = sparse_model([[1,0,0],[0,1,0],[0,0,1]],
                            [[0,None,None],[None,1,None],[None,None,2]],pi)
    check(min(verify_completion(rr,vv,0,{Q(i):[0,1,2] for i in range(3)})) == 0)
    # All-zero unused column and arbitrary null placeholders do not affect result.
    rr,vv,pp = sparse_model([[1,0],[1,0]],[[0,'ignored'],[1,None]],[Q(1,2)]*2)
    check(min(verify_completion(rr,vv,1,{Q(0):[0,123],Q(1):[1,-999]})) == 0)
    for denominator in range(2,22):
        for a in range(denominator+1):
            for b in range(denominator-a+1):
                q=[Q(a,denominator),Q(b,denominator),Q(denominator-a-b,denominator)]
                d,n=moments(r,v,q)
                check(n <= Q(16,9)*d)
    print(json.dumps(dict(checks=count,arithmetic='rational',assert_independent=True,
                         sparse_sharp_coefficient='16/9',last_edge_ratio=str(last_edge_ratio))))


if __name__ == '__main__':
    main()
