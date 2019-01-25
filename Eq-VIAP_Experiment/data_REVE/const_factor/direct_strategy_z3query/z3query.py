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
	p1x5=Function('p1x5',IntSort(),IntSort())
	_k1=Const('_k1',IntSort())
	_n2=Int('_n2')
	p2n=Int('p2n')
	p1x1=Int('p1x1')
	_N2=Const('_N2',IntSort())
	p1k5=Function('p1k5',IntSort(),IntSort())
	_N1=Const('_N1',IntSort())
	p2n1=Int('p2n1')
	p1n=Int('p1n')
	p1k1=Int('p1k1')
	p1x=Int('p1x')
	p1n1=Int('p1n1')
	p2x10=Function('p2x10',IntSort(),IntSort())
	p1i1=Int('p1i1')
	_k2=Const('_k2',IntSort())
	_n1=Int('_n1')
	p2k10=Function('p2k10',IntSort(),IntSort())
	p2i1=Int('p2i1')
	p2x1=Int('p2x1')
	p2x=Int('p2x')
	p2k1=Int('p2k1')
        k=Int('k')
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2n1 == p2n)
	_s.add(p1n1 == p1n)
	_s.add(p1i1 == _N1)
	_s.add(p1k1 == p1k5(_N1))
	_s.add(p2i1 == _N2)
	_s.add(p2k1 == p2k10(_N2))
	_s.add(p1x1 == p1x5(_N1))
	_s.add(p2x1 == p2x10(_N2))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1x5(_n1 + 1) == 5*p1k5(_n1) + p1x5(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1k5(_n1 + 1) == If(_n1 >= 5,p1k5(_n1) + 4,p1k5(_n1) + 1))))
	_s.add(p1x5(0) == p1x)
	_s.add(p1k5(0) == 0)
	_s.add(((_N1)==(p1n)))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),(_f(_n1)!=p1n))))
	_s.add(Or(_N1==0,(_N1 - 1!=p1n)))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2x10(_n2 + 1) == p2k10(_n2) + p2x10(_n2))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2k10(_n2 + 1) == If(_n2 >= 5,p2k10(_n2) + 20,p2k10(_n2) + 5))))
	_s.add(p2x10(0) == p2x)
	_s.add(p2k10(0) == 0)
	_s.add(((_N2)==(p2n)))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),(_f(_n2)!=p2n))))
	_s.add(Or(_N2==0,(_N2 - 1!=p2n)))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(And(((p1x)==(p2x)),((p1n)==(p2n))))
	_s.add(Not(((p1x5(_N1))==(p2x10(_N2)))))


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
