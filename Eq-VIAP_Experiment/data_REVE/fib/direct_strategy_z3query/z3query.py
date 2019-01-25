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
	p1n=Int('p1n')
	p2g1=Int('p2g1')
	p1g1=Int('p1g1')
	p1g4=Function('p1g4',IntSort(),IntSort())
	p2g8=Function('p2g8',IntSort(),IntSort())
	p2n=Int('p2n')
	_N2=Const('_N2',IntSort())
	_N1=Const('_N1',IntSort())
	p1h4=Function('p1h4',IntSort(),IntSort())
	p1n1=Int('p1n1')
	p1h1=Int('p1h1')
	p2h8=Function('p2h8',IntSort(),IntSort())
	p1n4=Function('p1n4',IntSort(),IntSort())
	p2h1=Int('p2h1')
	p2n8=Function('p2n8',IntSort(),IntSort())
	_k1=Const('_k1',IntSort())
	_n2=Int('_n2')
	_k2=Const('_k2',IntSort())
	_n1=Int('_n1')
	p2n1=Int('p2n1')
	p2f1=Int('p2f1')
	p1f1=Int('p1f1')
	p2f8=Function('p2f8',IntSort(),IntSort())
	p1f4=Function('p1f4',IntSort(),IntSort())
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2g1 == p2g8(_N2))
	_s.add(p2f1 == p2f8(_N2))
	_s.add(p1f1 == p1f4(_N1))
	_s.add(p1g1 == p1g4(_N1))
	_s.add(p1h1 == p1h4(_N1))
	_s.add(p2n1 == p2n8(_N2))
	_s.add(p2h1 == p2h8(_N2))
	_s.add(p1n1 == p1n4(_N1))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1h4(_n1 + 1) == p1f4(_n1) + p1g4(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1f4(_n1 + 1) == 1)))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1g4(_n1 + 1) == p1f4(_n1) + p1g4(_n1))))
	_s.add(p1h4(0) == 0)
	_s.add(p1f4(0) == 0)
	_s.add(p1g4(0) == 1)
	_s.add(0 <= -p1n+_N1)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),p1n-_n1 > 0)))
	_s.add(Or(_N1==0,p1n-_N1 + 1 > 0))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2g8(_n2 + 1) == p2f8(_n2) + p2g8(_n2))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2h8(_n2 + 1) == p2f8(_n2) + p2g8(_n2))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2f8(_n2 + 1) == p2g8(_n2))))
	_s.add(p2g8(0) == 1)
	_s.add(p2h8(0) == 0)
	_s.add(p2f8(0) == 1)
	_s.add(0 <= -p2n+_N2)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),p2n-_n2 > 0)))
	_s.add(Or(_N2==0,p2n-_N2 + 1 > 0))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((p1n)==(p2n)))
	_s.add(Not(((p1g4(_N1))==(p2g8(_N2)))))

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