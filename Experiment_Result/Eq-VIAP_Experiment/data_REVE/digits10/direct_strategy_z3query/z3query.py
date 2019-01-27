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
	p2b25=Function('p2b25',IntSort(),IntSort())
	_k1=Const('_k1',IntSort())
	_n2=Int('_n2')
	_k2=Const('_k2',IntSort())
	_n1=Int('_n1')
	_N2=Const('_N2',IntSort())
	p1result11=Function('p1result11',IntSort(),IntSort())
	_N1=Const('_N1',IntSort())
	p2n=Int('p2n')
	p2n1=Int('p2n1')
	p2n25=Function('p2n25',IntSort(),IntSort())
	p1n1=Int('p1n1')
	p2result25=Function('p2result25',IntSort(),IntSort())
	p1result1=Int('p1result1')
	p1n=Int('p1n')
	p1n11=Function('p1n11',IntSort(),IntSort())
	p2result1=Int('p2result1')
	p2b1=Int('p2b1')
	p2retval1=Int('p2retval1')
	p2retval25=Function('p2retval25',IntSort(),IntSort())
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2retval1 == p2retval25(_N2))
	_s.add(p1result1 == p1result11(_N1))
	_s.add(p2b1 == p2b25(_N2))
	_s.add(p2n1 == p2n25(_N2))
	_s.add(p2result1 == p2result25(_N2))
	_s.add(p1n1 == p1n11(_N1))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1result11(_n1 + 1) == If(((((p1n11(_n1))/(10)))>(0)),If(((((((p1n11(_n1))/(10)))/(10)))>(0)),If(((((((((p1n11(_n1))/(10)))/(10)))/(10)))>(0)),((((((((p1result11(_n1))+(1)))+(1)))+(1)))+(1)),((((((p1result11(_n1))+(1)))+(1)))+(1))),((((p1result11(_n1))+(1)))+(1))),((p1result11(_n1))+(1))))))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1n11(_n1 + 1) == If(((((p1n11(_n1))/(10)))>(0)),If(((((((p1n11(_n1))/(10)))/(10)))>(0)),If(((((((((p1n11(_n1))/(10)))/(10)))/(10)))>(0)),((((((((p1n11(_n1))/(10)))/(10)))/(10)))/(10)),((((((p1n11(_n1))/(10)))/(10)))/(10))),((((p1n11(_n1))/(10)))/(10))),((p1n11(_n1))/(10))))))
	_s.add(p1result11(0) == 1)
	_s.add(p1n11(0) == ((p1n)/(10)))
	_s.add(0 <= -p1n11(_N1))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),p1n11(_f(_n1)) > 0)))
	_s.add(Or(_N1==0,p1n11(_N1 - 1) > 0))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2n25(_n2 + 1) == If(p2n25(_n2) < 10,p2n25(_n2),If(p2n25(_n2) < 100,p2n25(_n2),If(p2n25(_n2) < 1000,p2n25(_n2),If(p2n25(_n2) < 10000,p2n25(_n2),((p2n25(_n2))/(10000)))))))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2retval25(_n2 + 1) == If(p2n25(_n2) < 10,p2result25(_n2),If(p2n25(_n2) < 100,((p2result25(_n2))+(1)),If(p2n25(_n2) < 1000,((p2result25(_n2))+(2)),If(p2n25(_n2) < 10000,((p2result25(_n2))+(3)),p2retval25(_n2))))))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2result25(_n2 + 1) == If(p2n25(_n2) < 10,p2result25(_n2),If(p2n25(_n2) < 100,p2result25(_n2),If(p2n25(_n2) < 1000,p2result25(_n2),If(p2n25(_n2) < 10000,p2result25(_n2),((p2result25(_n2))+(4)))))))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2b25(_n2 + 1) == If(p2n25(_n2) < 10,0,If(p2n25(_n2) < 100,0,If(p2n25(_n2) < 1000,0,If(p2n25(_n2) < 10000,0,p2b25(_n2))))))))
	_s.add(p2n25(0) == p2n)
	_s.add(p2retval25(0) == -1)
	_s.add(p2result25(0) == 1)
	_s.add(p2b25(0) == 1)
	_s.add(((p2b25(_N2))==((0))))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),(p2b25(_f(_n2))!=(0)))))
	_s.add(Or(_N2==0,(p2b25(_N2 - 1)!=(0))))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((p1n)==(p2n)))
	_s.add(Not(((p1result11(0))==(p2retval25(0)))))

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
