"""Independent exact arithmetic certificate for a vector-target obstruction."""
from fractions import Fraction as F
from itertools import combinations
r=[[F(z,100) for z in row] for row in [[2,43,55],[40,9,51],[46,53,1]]]
v=[[[F(z,10) for z in cell] for cell in row] for row in [[[3,-3],[18,5],[13,8]],[[-10,8],[8,-2],[-21,-4]],[[14,-17],[2,-12],[-6,3]]]]
x=[[sum(r[i][b]*v[i][b][k] for b in range(3)) for k in range(2)] for i in range(3)]
sq=lambda w:sum(z*z for z in w)
diff=lambda a,b:[z-w for z,w in zip(a,b)]
q=[F(1,3)]*3
t=[sum(q[i]*x[i][k] for i in range(3)) for k in range(2)]
D=sum(q[i]*sq(diff(x[i],t)) for i in range(3))
N=sum(sum(q[i]*r[i][b]*sq(v[i][b]) for i in range(3))-sq([sum(q[i]*r[i][b]*v[i][b][k] for i in range(3)) for k in range(2)])/sum(q[i]*r[i][b] for i in range(3)) for b in range(3))
ratios=[]
print('x',x)
for i in range(3):
 for j in range(3):
  if i==j:continue
  den=sq(diff(x[i],x[j]))
  num=sum(r[i][b]*sq(diff(v[i][b],v[j][b])) for b in range(3))
  margin=den-num
  print('pair',i,j,'margin',margin,'ratio',num/den)
  if margin<=0:raise ValueError('pair failed')
  ratios.append(num/den)
print('D',D,'N',N,'gap',D-N,'R',max(ratios),'N/D',N/D)
if not N>D:raise ValueError('no violation')
VA=sum(q[i]*sq(x[i]) for i in range(3))
VAB=sum(q[i]*r[i][b]*sq(v[i][b]) for i in range(3) for b in range(3))
VB=F(0)
for b in range(3):
 p=sum(q[i]*r[i][b] for i in range(3))
 mu=[sum(q[i]*r[i][b]*v[i][b][k] for i in range(3))/p for k in range(2)]
 VB+=p*sq(mu)
V0=sq(t)
gap=VB-V0-VAB+VA
if gap!=D-N:raise ValueError('score mismatch')
print('scores VA,VAB,VB,V0',VA,VAB,VB,V0,'gap',gap)
categorical=[]
categorical_checks=0
for row in v:
 crow=[]
 for a,b in row:
  probs=[F(1,4)+a/20,F(1,4)-a/20,F(1,4)+b/20,F(1,4)-b/20]
  if min(probs)<=0 or sum(probs)!=1:raise ValueError('invalid categorical embedding')
  categorical_checks+=1
  crow.append(probs)
 categorical.append(crow)
# Recompute in four dimensions, rather than assuming the affine scaling.
cx=[[sum(r[i][b]*categorical[i][b][k] for b in range(3)) for k in range(4)] for i in range(3)]
ct=[sum(q[i]*cx[i][k] for i in range(3)) for k in range(4)]
cD=sum(q[i]*sq(diff(cx[i],ct)) for i in range(3))
cN=F(0)
cVB=F(0)
for b in range(3):
 p=sum(q[i]*r[i][b] for i in range(3))
 mu=[sum(q[i]*r[i][b]*categorical[i][b][k] for i in range(3))/p for k in range(4)]
 cN+=sum(q[i]*r[i][b]*sq(diff(categorical[i][b],mu)) for i in range(3))
 cVB+=p*sq(mu)
for actual,expected in [(cD,D/200),(cN,N/200),(cD-cN,(D-N)/200)]:
 if actual!=expected:raise ValueError('categorical residual scaling failed')
 categorical_checks+=1
for i in range(3):
 for j in range(3):
  if i==j:continue
  cmargin=sq(diff(cx[i],cx[j]))-sum(r[i][b]*sq(diff(categorical[i][b],categorical[j][b])) for b in range(3))
  original=sq(diff(x[i],x[j]))-sum(r[i][b]*sq(diff(v[i][b],v[j][b])) for b in range(3))
  if cmargin!=original/200 or cmargin<=0:raise ValueError('categorical margin scaling failed')
  categorical_checks+=1
cVA=sum(q[i]*sq(cx[i]) for i in range(3))
cVAB=sum(q[i]*r[i][b]*sq(categorical[i][b]) for i in range(3) for b in range(3))
cV0=sq(ct)
cgap=cVB-cV0-cVAB+cVA
if cgap!=cD-cN or cgap!=gap/200 or cgap>=0:raise ValueError('categorical score mismatch')
categorical_checks+=1
print('categorical checks',categorical_checks,'D',cD,'N',cN,'gap',cgap,'scale',F(1,200))
print('PASS: positive full support, all six strict directed tests, negative global gap')
