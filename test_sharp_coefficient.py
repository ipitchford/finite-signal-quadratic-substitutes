"""Exact supplementary checks of the manuscript's full-support sharp coefficient.

See paper.tex, section "Model and the full-support sharp coefficient".
These finite checks are not a proof and require no historical development notes.
Uses explicit exceptions so checks remain active under Python -O.
Prints results; never overwrites historical receipts.
"""
import json
from fractions import Fraction as Q
from exact import model, means, residual, direct_gap


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def coefficient(r, v):
    x = means(r, v)
    ratios = []
    for i in range(len(r)):
        for j in range(len(r)):
            numerator = sum(r[i][b] * (v[i][b] - v[j][b])**2
                            for b in range(len(r[0])))
            if x[i] == x[j]:
                if numerator:
                    return None, (i, j)
            else:
                ratios.append((numerator / (x[i] - x[j])**2, (i, j)))
    return max(ratios, default=(Q(0), None))


def variance(x, q):
    return sum(a*b*b for a, b in zip(q, x)) - sum(a*b for a, b in zip(q, x))**2


def embed(q, pi):
    alpha = min(p/a for p, a in zip(pi, q) if a) / 2
    kernel = []
    for i, (p, a) in enumerate(zip(pi, q)):
        row = [alpha*a/p] + [Q(0)]*len(q)
        row[i+1] = 1-row[0]
        require(sum(row) == 1 and min(row) >= 0, 'Invalid channel')
        kernel.append(row)
    return alpha, kernel


def main():
    good = model([['4/5','1/10','1/10'],['1/10','4/5','1/10'],
                  ['1/10','1/10','4/5']],
                 [[Q(i+b,4) for b in range(3)] for i in range(3)], ['1/3']*3)
    bad = model([['1/2','1/2']]*2, [[0,0],[0,1]], ['1/3','2/3'])
    infinite = model([['1/2','1/2']]*2, [[0,1],[1,0]], ['1/3','2/3'])
    constant = model([['1/2','1/2']]*2, [[1,1],[1,1]], ['1/3','2/3'])
    require(coefficient(*good[:2])[0] == Q(100,289), 'Positive example coefficient')
    require(coefficient(*bad[:2])[0] == 2, 'Violation coefficient')
    require(coefficient(*infinite[:2])[0] is None, 'Infinite coefficient')
    require(coefficient(*constant[:2])[0] == 0, 'Constant coefficient')
    require(residual(*infinite[:2], [Q(1,2)]*2) < 0, 'Equal means obstruction')
    checks = 5
    # Equal means may share a nonconstant vector while retaining different norms.
    repeated = model([['1/4','1/2','1/4'], ['1/3']*3, ['1/3']*3],
                     [[0,1,2], [0,1,2], [1,2,3]], ['1/3']*3)
    rr,vv,pp = repeated
    require(means(rr,vv) == [Q(1),Q(1),Q(2)], 'Repeated means fixture')
    require(coefficient(rr,vv)[0] == 1, 'Repeated means coefficient')
    for q in [[Q(1,3)]*3, [Q(1,2),Q(1,4),Q(1,4)], [Q(1,2),Q(1,2),Q(0)]]:
        require(residual(rr,vv,q) >= 0, 'Repeated means posterior bound')
    r,v,pi = good
    D = variance(means(r,v),pi)
    require(D == Q(289,2400), 'No-disclosure source-value loss')
    require(residual(r,v,pi) >= Q(63,800), 'No-disclosure worked bound')
    checks += 7
    records = []
    for name, (r,v,pi) in [('positive',good), ('violation',bad)]:
        R, (i,j) = coefficient(r,v)
        x = means(r,v)
        for denominator in [2,10,100,1000,10000]:
            s = Q(1,denominator)
            q = [Q(0)]*len(r)
            q[j],q[i] = 1-s,s
            D = variance(x,q)
            F = residual(r,v,q)
            ratio = (D-F)/D
            require(ratio <= R, 'Sharp upper bound violated')
            alpha,kernel = embed(q,pi)
            gap = direct_gap(r,v,pi,kernel)
            require(gap == alpha*F, 'Direct score disagrees with posterior identity')
            require(gap/(alpha*D) == 1-ratio, 'Normalized channel ratio')
            checks += 3
            records.append(dict(model=name,s=str(s),ratio=str(ratio),
                                bound=str(R),normalized_gap=str(1-ratio)))
        require(abs(R-ratio) < Q(1,1000), 'Edge sequence not near sharp bound')
        checks += 1
    # Semantic negative control: the sharp coefficient cannot be decreased.
    r,v,pi = bad
    q = [Q(1,2),Q(1,2)]
    D = variance(means(r,v),q)
    N = D-residual(r,v,q)
    require(N > Q(3,2)*D, 'Weakened-coefficient negative control failed')
    checks += 1
    print(json.dumps(dict(checks=checks,checks_use_assert=False,edge_sequences=records),indent=2))


if __name__ == '__main__':
    main()
