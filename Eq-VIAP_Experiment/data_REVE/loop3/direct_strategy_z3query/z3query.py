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
	_n2=Int('_n2')
	p2n=Int('p2n')
	_N2=Const('_N2',IntSort())
	p1i1=Int('p1i1')
	p2n1=Int('p2n1')
	p1j1=Int('p1j1')
	p2j1=Int('p2j1')
	p1n1=Int('p1n1')
	p1n=Int('p1n')
	_N1=Const('_N1',IntSort())
	p2i1=Int('p2i1')
	_n1=Int('_n1')
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p1i1 == _N1 + 1)
	_s.add(p1j1 == 2*_N1)
	_s.add(p2n1 == If(p2n < 1,1,p2n))
	_s.add(p2i1 == _N2 + 1)
	_s.add(p1n1 == If(p1n < 1,1,p1n))
	_s.add(p2j1 == 2*_N2 + 2)
	_s.add(((_N1 + 1)>(If(p1n < 1,1,p1n))))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),((_f(_n1) + 1)<=(If(p1n < 1,1,p1n))))))
	_s.add(Or(_N1==0,(((_N1-1) + 1)<=(If(p1n < 1,1,p1n)))))
	_s.add(((_N2)>=(((-1)+(If(p2n < 1,1,p2n))))))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),((_f(_n2) + 1)<(If(p2n < 1,1,p2n))))))
	_s.add(Or(_N2==0,(((_N2-1) + 1)<(If(p2n < 1,1,p2n)))))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((p1n)==(p2n)))
	_s.add(Not(((2*_N1)==(2*_N2 + 2))))

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
