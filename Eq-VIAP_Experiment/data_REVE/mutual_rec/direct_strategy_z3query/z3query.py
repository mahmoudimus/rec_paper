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
	_k2=Const('_k2',IntSort())
	_n1=Int('_n1')
	p1l=Int('p1l')
	p1m=Int('p1m')
	p2m1=Int('p2m1')
	p1m4=Function('p1m4',IntSort(),IntSort())
	p2m8=Function('p2m8',IntSort(),IntSort())
	p1m1=Int('p1m1')
	p1x4=Function('p1x4',IntSort(),IntSort())
	__VERIFIER_nondet_int3=Function('__VERIFIER_nondet_int3',IntSort(),IntSort())
	__VERIFIER_nondet_int2=Function('__VERIFIER_nondet_int2',IntSort(),IntSort())
	p1x1=Int('p1x1')
	p2x8=Function('p2x8',IntSort(),IntSort())
	p2x1=Int('p2x1')
	p2m=Int('p2m')
	_N2=Const('_N2',IntSort())
	p2l=Int('p2l')
	_N1=Const('_N1',IntSort())
	p1l1=Int('p1l1')
	p1l4=Function('p1l4',IntSort(),IntSort())
	p2y8=Function('p2y8',IntSort(),IntSort())
	p2l8=Function('p2l8',IntSort(),IntSort())
	p2y1=Int('p2y1')
	p2l1=Int('p2l1')
	_k1=Const('_k1',IntSort())
	_n2=Int('_n2')
	p1y1=Int('p1y1')
	p1y4=Function('p1y4',IntSort(),IntSort())
        power=Function('power',IntSort(),IntSort(),IntSort())
	main=Int('main')
	_s=Solver()
        _s.add(ForAll([_p1],Implies(_p1>=0, power(0,_p1)==0)))
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
        _s.add(ForAll([_p1,_p2],Implies(power(_p2,_p1)==0,_p2==0)))
        _s.add(ForAll([_p1],Implies(_p1>0, power(_p1,0)==1)))
        _s.add(ForAll([_p1,_p2],Implies(power(_p1,_p2)==1,Or(_p1==1,_p2==0))))
        _s.add(ForAll([_p1,_p2],Implies(And(_p1>0,_p2>=0), power(_p1,_p2+1)==power(_p1,_p2)*_p1)))
	_s.set("timeout",50000)
	_s.add(p2m1 == p2m8(_N2))
	_s.add(p2l1 == p2l8(_N2))
	_s.add(p1l1 == p1l4(_N1))
	_s.add(p1m1 == p1m4(_N1))
	_s.add(p1x1 == If(_N1==0,1,power(2,_N1)))
	_s.add(p1y1 == If(_N1==0,1,power(2,_N1)))
	_s.add(p2y1 == If(_N2==0,1,power(2,_N2)))
	_s.add(p2x1 == If(_N2==0,1,power(2,_N2)))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1l4(_n1 + 1) == If(_n1==0,1,power(2,_n1)))))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1m4(_n1 + 1) == If(_n1==0,1,power(2,_n1)))))
	_s.add(p1l4(0) == p1l)
	_s.add(p1m4(0) == p1m)
	_s.add(((0)<=(-(__VERIFIER_nondet_int2(_N1)))))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),((__VERIFIER_nondet_int2(_n1))>(0)))))
	_s.add(Or(_N1==0,((__VERIFIER_nondet_int2((_N1-1)))>(0))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p1l4(_n2 + 1) == If(_n2==0,2,power(2,_n2+1)))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p1m4(_n2 + 1) == If(_n2==0,2,power(2,_n2+1)))))
	_s.add(p2m8(0) == p2m)
	_s.add(p2l8(0) == p2l)
	_s.add(((0)<=(-(__VERIFIER_nondet_int3(_N2)))))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),((__VERIFIER_nondet_int3(_n2))>(0)))))
	_s.add(Or(_N2==0,((__VERIFIER_nondet_int3((_N2-1)))>(0))))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
        _s.add(ForAll([_n2],Implies(_n2>=0,__VERIFIER_nondet_int2(_n2)==__VERIFIER_nondet_int3(_n2))))
	_s.add(Not(((If(_N1==0,1,power(2,_N1))==(If(_N2==0,1,power(2,_N2)))))))

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
