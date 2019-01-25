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
	p1i1=Int('p1i1')
	p1x1=Int('p1x1')
	_n1=Int('_n1')
	_N2=Const('_N2',IntSort())
	_N3=Const('_N3',IntSort())
	p2n=Int('p2n')
	_N6=Const('_N6',IntSort())
	p2n1=Int('p2n1')
	p1n=Int('p1n')
	p2x1=Int('p2x1')
	_n2=Int('_n2')
	p1n1=Int('p1n1')
	_n5=Int('_n5')
	_N4=Const('_N4',IntSort())
	_N1=Const('_N1',IntSort())
	_n3=Int('_n3')
	p2i1=Int('p2i1')
	_n6=Int('_n6')
	_N5=Const('_N5',IntSort())
	_n4=Int('_n4')
	main=Int('main')
	power=Function('power',IntSort(),IntSort(),IntSort())
	power=Function('power',RealSort(),RealSort(),RealSort())
	_s=Solver()
	_s.add(ForAll([_p1],Implies(_p1>=0, power(0,_p1)==0)))
	_s.add(ForAll([_p1,_p2],Implies(power(_p2,_p1)==0,_p2==0)))
	_s.add(ForAll([_p1],Implies(_p1>0, power(_p1,0)==1)))
	_s.add(ForAll([_p1,_p2],Implies(power(_p1,_p2)==1,Or(_p1==1,_p2==0))))
	_s.add(ForAll([_p1,_p2],Implies(And(_p1>0,_p2>=0), power(_p1,_p2+1)==power(_p1,_p2)*_p1)))
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2n1 == p2n)
	_s.add(p1n1 == p1n)
	_s.add(p1x1 == ((power((2),(_N3)))*(((-_N2 + _N2*_N2 + 2)/(2)))))
	_s.add(p1i1 == _N3 + 1)
	_s.add(p2i1 == _N6 + 1)
	_s.add(p2x1 == ((power((2),(_N6)))*(((_N5 + _N5*_N5 + 2)/(2)))))
	_s.add(_N1 + 1 > p1n)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),_f(_n1) + 1 <= p1n)))
	_s.add(Or(_N1==0,_N1 <= p1n))
	_s.add(_N2 > p1n)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) <= p1n)))
	_s.add(Or(_N2==0,_N2 - 1 <= p1n))
	_s.add(_N3 + 1 > p1n)
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),_f(_n3) + 1 <= p1n)))
	_s.add(Or(_N3==0,_N3 <= p1n))
	_s.add(_N4 + 1 > p2n)
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),_f(_n4) + 1 <= p2n)))
	_s.add(Or(_N4==0,_N4 <= p2n))
	_s.add(_N5 + 1 > p2n)
	_s.add(ForAll([_n5],Implies(And(_n5 < _N5,_n5>=0),_f(_n5) + 1 <= p2n)))
	_s.add(Or(_N5==0,_N5 <= p2n))
	_s.add(_N6 + 1 > p2n)
	_s.add(ForAll([_n6],Implies(And(_n6 < _N6,_n6>=0),_f(_n6) + 1 <= p2n)))
	_s.add(Or(_N6==0,_N6 <= p2n))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(_N4>=0)
	_s.add(_N5>=0)
	_s.add(_N6>=0)
	_s.add(((p1n)==(p2n)))
	_s.add(Not(((((power((2),(_N3)))*(((-_N2 + _N2*_N2 + 2)/(2)))))==(((power((2),(_N6)))*(((_N5 + _N5*_N5 + 2)/(2))))))))

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