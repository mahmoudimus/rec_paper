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
	p2i10=Function('p2i10',IntSort(),IntSort())
	break_2_flag10=Function('break_2_flag10',IntSort(),IntSort())
	_N1=Const('_N1',IntSort())
	p1x1=Int('p1x1')
	_n1=Int('_n1')
	_N2=Const('_N2',IntSort())
	p1i1=Int('p1i1')
	p2x1=Int('p2x1')
	p2i1=Int('p2i1')
	break_1_flag1=Int('break_1_flag1')
	_n2=Int('_n2')
	break_1_flag5=Function('break_1_flag5',IntSort(),IntSort())
	p1x=Int('p1x')
	break_2_flag1=Int('break_2_flag1')
	p1i5=Function('p1i5',IntSort(),IntSort())
	p2x=Int('p2x')
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p1x1 == p1x)
	_s.add(p2x1 == p2x)
	_s.add(p1i1 == p1i5(_N1))
	_s.add(break_2_flag1 == break_2_flag10(_N2))
	_s.add(p2i1 == p2i10(_N2))
	_s.add(break_1_flag1 == break_1_flag5(_N1))
	_s.add(ForAll([_n1],Implies(_n1>=0,p1i5(_n1 + 1) == If(((If(((p1i5(_n1))==(p1x)),1,0))==(0)),p1i5(_n1) + 1,p1i5(_n1)))))
	_s.add(ForAll([_n1],Implies(_n1>=0,break_1_flag5(_n1 + 1) == If(((p1i5(_n1))==(p1x)),1,0))))
	_s.add(p1i5(0) == 0)
	_s.add(break_1_flag5(0) == 0)
	_s.add(Or(p1i5(_N1) > 10,((break_1_flag5(_N1))!=(0))))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),And(p1i5(_f(_n1)) <= 10,((break_1_flag5(_f(_n1)))==(0))))))
	_s.add(Or(_N1==0,And(p1i5((_N1-1)) <= 10,((break_1_flag5((_N1-1)))==(0)))))
	_s.add(ForAll([_n2],Implies(_n2>=0,break_2_flag10(_n2 + 1) == If(((p2i10(_n2))==(-p2x + 10)),1,0))))
	_s.add(ForAll([_n2],Implies(_n2>=0,p2i10(_n2 + 1) == If(((If(((p2i10(_n2))==(-p2x + 10)),1,0))==(0)),p2i10(_n2) - 1,p2i10(_n2)))))
	_s.add(break_2_flag10(0) == 0)
	_s.add(p2i10(0) == 10)
	_s.add(Or(p2i10(_N2) < 0,((break_2_flag10(_N2))!=(0))))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),And(p2i10(_f(_n2)) >= 0,((break_2_flag10(_f(_n2)))==(0))))))
	_s.add(Or(_N2==0,And(p2i10((_N2-1)) >= 0,((break_2_flag10((_N2-1)))==(0)))))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((p1x)==(p2x)))
	_s.add(Not(((p1i5(_N1))==(-p2i10(_N2) + 10))))

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