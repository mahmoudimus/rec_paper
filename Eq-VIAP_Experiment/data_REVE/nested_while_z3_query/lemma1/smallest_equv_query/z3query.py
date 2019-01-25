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
	p1g=Int('p1g')
	p2i1=Int('p2i1')
	p1x=Int('p1x')
	p1x7=Function('p1x7',IntSort(),IntSort())
	p1x1=Int('p1x1')
	p2g14=Function('p2g14',IntSort(),IntSort())
	p1i1=Int('p1i1')
	p2x1=Int('p2x1')
	p2g1=Int('p2g1')
	p1g1=Int('p1g1')
	p1g7=Function('p1g7',IntSort(),IntSort())
	p2g=Int('p2g')
	_N2=Const('_N2',IntSort())
	_N3=Function('_N3',IntSort(),IntSort())
	_N1=Function('_N1',IntSort(),IntSort())
	_N4=Const('_N4',IntSort())
	p2x=Int('p2x')
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	_n4=Int('_n4')
        _k1=Int('_k1')
	p2x14=Function('p2x14',IntSort(),IntSort())
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2g1 == p2g14(_N4))
	_s.add(p1g1 == p1g7(_N2))
	_s.add(p1i1 == _N2)
	_s.add(p2i1 == _N4)
	_s.add(p1x1 == p1x7(_N2))
	_s.add(p2x1 == p2x14(_N4))
	_s.add(ForAll([_n2],Implies(_n2>=0,_N1(_n2) >= _n2 - p1x7(_n2) + 1)))
        
	_s.add(ForAll([_n1,_n2],Implies(And(_n1 < _N1(_n2),And(_n1>=0,_n2>=0)),_n1 < _n2 - p1x7(_n2) + 1)))
        
	_s.add(ForAll([_n2],Implies(_n2>=0,Or(_N1(_n2)==0,_N1(_n2) + p1x7(_n2) - 1 < _n2 + 1))))
        
	_s.add(ForAll([_n2],Implies(_n2>=0,p1x7(_n2 + 1) == _N1(_n2) + p1x7(_n2))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p1g7(_n2 + 1) == _N1(_n2) + p1g7(_n2) - 1)))
	_s.add(p1x7(0) == p1x)
	_s.add(p1g7(0) == p1g)
	_s.add(_N2 >= p1x7(_N2))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_n2 < p1x7(_n2))))
        
	_s.add(Or(_N2==0,_N2 - 1 < p1x7(_N2 - 1)))
        
	_s.add(ForAll([_n4],Implies(_n4>=0,_N3(_n4) >= _n4 - p2x14(_n4) + 1)))
        
	_s.add(ForAll([_n4,_n3],Implies(And(_n3 < _N3(_n4),And(_n4>=0,_n3>=0)),_n3 < _n4 - p2x14(_n4) + 1)))
                
	_s.add(ForAll([_n4,_n3],Implies(And(_n3 < _N3(_n4),And(_n4>=0,_n3>=0)),_n3 + p2x14(_n4) < _n4 + 1)))
        
	_s.add(ForAll([_n4],Implies(_n4>=0,Or(_N3(_n4)==0,_N3(_n4) + p2x14(_n4) - 1 < _n4 + 1))))
	_s.add(ForAll([_n4],Implies(_n4>=0,p2g14(_n4 + 1) == _N3(_n4) + p2g14(_n4) - 1)))
	_s.add(ForAll([_n4],Implies(_n4>=0,p2x14(_n4 + 1) == _N3(_n4) + p2x14(_n4))))
	_s.add(p2g14(0) == p2g)
	_s.add(p2x14(0) == p2x)
	_s.add(_N4 >= p2x14(_N4))
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),_n4 < p2x14(_n4))))
	_s.add(Or(_N4==0,_N4 - 1 < p2x14(_N4 - 1)))
	_s.add(ForAll([_n2],_N1(_n2)>=0))
	_s.add(_N2>=0)
	_s.add(ForAll([_n4],_N3(_n4)>=0))
	_s.add(_N4>=0)
	_s.add(And((((p1x)==(p2x))),(((p1g)==(p2g)))))
        _s.add(Not(And(ForAll([_n2],Implies(_n2>=0,_N1(_n2) >= _n2 - p1x7(_n2) + 1)),ForAll([_n1,_n2],Implies(And(_n1 < _N1(_n2),And(_n1>=0,_n2>=0)),_n1 < _n2 - p1x7(_n2) + 1)))==And(ForAll([_n2],Implies(_n2>=0,_N3(_n2) >= _n2 - p2x14(_n2) + 1)),ForAll([_n2,_n3],Implies(And(_n3 < _N3(_n2),And(_n2>=0,_n3>=0)),_n3 < _n2 - p2x14(_n2) + 1)))))
        
        

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
