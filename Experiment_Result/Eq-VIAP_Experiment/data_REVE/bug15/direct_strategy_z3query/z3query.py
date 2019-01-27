import sys
import os
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/setuptools/")
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/z3/python/")
from z3 import *
init(currentdirectory+"/packages/z3")

try:
	_p1=Int('_p1')
	_p2=Int('_p2')
	_n=Int('_n')
	_bool=Int('_bool')
	arraySort = DeclareSort('arraySort')
	_f=Function('_f',IntSort(),IntSort())
	_ToReal=Function('_ToReal',RealSort(),IntSort())
	_ToInt=Function('_ToInt',IntSort(),RealSort())
	p2z1=Int('p2z1')
	_n1=Int('_n1')
	p1x1=Int('p1x1')
	p2y1=Int('p2y1')
	_N1=Const('_N1',IntSort())
	p2y4=Function('p2y4',IntSort(),IntSort())
	p2x1=Int('p2x1')
	_N2=Const('_N2',IntSort())
	_n2=Int('_n2')
	p1y2=Function('p1y2',IntSort(),IntSort())
	p1z=Int('p1z')
	p1y1=Int('p1y1')
	p1z1=Int('p1z1')
	p2z=Int('p2z')
	main=Int('main')
	power=Function('power',RealSort(),RealSort(),RealSort())
	_s=Solver()
	_s.add(ForAll([_p1],Implies(_p1>=0, power(0,_p1)==0)))
	_s.add(ForAll([_p1,_p2],Implies(power(_p2,_p1)==0,_p2==0)))
	_s.add(ForAll([_p1],Implies(_p1>0, power(_p1,0)==1)))
	_s.add(ForAll([_p1,_p2],Implies(power(_p1,_p2)==1,Or(_p1==1,_p2==0))))
	_s.add(ForAll([_p1,_p2],Implies(And(_p1>0,_p2>=0), power(_p1,_p2+1)==power(_p1,_p2)*_p1)))
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p1z1 == p1z)
	_s.add(p2z1 == p2z)
	_s.add(p1x1 == ((((((power((2),(_N1)))*(1)))+(power((2),(_N1 + 2)))))-(4)))
	_s.add(p1y1 == p1y2(_N1))
	_s.add(p2y1 == p2y4(_N2))
	_s.add(p2x1 == ((((((power((2),(_N2)))*(1)))+(power((2),(_N2 + 2)))))-(4)))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1y2(_n1 + 1) == ((2)+(((((((power((2),(_n1)))*(1)))+(power((2),(_n1 + 2)))))-(4)))))))
	_s.add(p1y2(0) == 0)
	_s.add(((((((((power((2),(_N1)))*(1)))+(power((2),(_N1 + 2)))))-(4)))>=(10)))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),((((((((power((2),(_f(_n1))))*(1)))+(power((2),(_f(_n1) + 2)))))-(4)))<(10)))))
	_s.add(Or(_N1==0,((((((((power((2),((_N1-1))))*(1)))+(power((2),((_N1-1) + 2)))))-(4)))<(10))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2y4(_n2 + 1) == ((((((((power((2),(_n2)))*(1)))+(power((2),(_n2 + 2)))))-(4)))+(2)))))
	_s.add(p2y4(0) == 0)
	_s.add(((((((((power((2),(_N2)))*(1)))+(power((2),(_N2 + 2)))))-(4)))>(9)))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),((((((((power((2),(_f(_n2))))*(1)))+(power((2),(_f(_n2) + 2)))))-(4)))<=(9)))))
	_s.add(Or(_N2==0,((((((((power((2),((_N2-1))))*(1)))+(power((2),((_N2-1) + 2)))))-(4)))<=(9))))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((p1z)==(p2z)))
	_s.add(Not((((((((((((power((2),(_N1)))*(1)))+(power((2),(_N1 + 2)))))-(4)))*(2))))==((((2)*(((((((power((2),(_N2)))*(1)))+(power((2),(_N2 + 2)))))-(4)))))))))

except Exception as e:
	print "Error(Z3Query)"
	sys.exit(1)

try:
	result=_s.check()
	if sat==result:
		print "Counter Example"
		print _s.model()
	elif unsat==result:
		result
		print "Successfully Proved"
	else:
		print "Failed To Prove"
except Exception as e:
	print "Error(Z3Query)"
