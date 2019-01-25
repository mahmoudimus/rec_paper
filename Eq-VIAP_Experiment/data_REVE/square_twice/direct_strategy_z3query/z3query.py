import sys
import os
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/setuptools/")
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/z3/python/")
from z3 import *
init(currentdirectory+"/packages/z3")
set_param(proof=True)

try:
	_p1=Int('_p1')
	_p2=Int('_p2')
	_n=Int('_n')
	_bool=Int('_bool')
	arraySort = DeclareSort('arraySort')
	_f=Function('_f',IntSort(),IntSort())
	_ToReal=Function('_ToReal',RealSort(),IntSort())
	_ToInt=Function('_ToInt',IntSort(),RealSort())
	_n2=Int('_n2')
	p1i1=Int('p1i1')
	p1r1=Int('p1r1')
	_N2=Const('_N2',IntSort())
	_N3=Const('_N3',IntSort())
	_n3=Int('_n3')
	p2n=Int('p2n')
	p2n1=Int('p2n1')
	p1i4=Function('p1i4',IntSort(),IntSort())
	p1i2=Function('p1i2',IntSort(),IntSort())
	p1n1=Int('p1n1')
	p1n=Int('p1n')
	_N1=Const('_N1',IntSort())
	p2r1=Int('p2r1')
	p2i1=Int('p2i1')
	_n1=Int('_n1')
	p2i6=Function('p2i6',IntSort(),IntSort())
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2n1 == p2n)
	_s.add(p1i1 == p1n-_N2)
	_s.add(p1r1 == _N2*p1n)
	_s.add(p2i1 == p2n-_N3)
	_s.add(p1n1 == _N1*p1n)
	_s.add(p2r1 == _N3*p2n)
	_s.add(0 <= -p1n+_N1)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),p1n-_n1 > 0)))
	_s.add(Or(_N1==0,p1n-_N1 + 1 > 0))
	_s.add(0 <= -p1n+_N2)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),p1n-_n2 > 0)))
	_s.add(Or(_N2==0,p1n-_N2 + 1 > 0))
	_s.add(0 <= -p2n+_N3)
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),p2n-_n3 > 0)))
	_s.add(Or(_N3==0,p2n-_N3 + 1 > 0))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(((p1n)==(p2n)))
	_s.add(Not(((_N2*p1n)==(_N3*p2n))))

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
