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
	p2t1=Int('p2t1')
	p1x1=Int('p1x1')
	p2c=Int('p2c')
	p2x6=Function('p2x6',IntSort(),IntSort())
	_N2=Const('_N2',IntSort())
	_N1=Const('_N1',IntSort())
	p2x1=Int('p2x1')
	p1t1=Int('p1t1')
	p2t=Int('p2t')
	p1c=Int('p1c')
	p1t=Int('p1t')
	p1c1=Int('p1c1')
	p1c2=Function('p1c2',IntSort(),IntSort())
	p2c1=Int('p2c1')
	_n1=Int('_n1')
	p2c6=Function('p2c6',IntSort(),IntSort())
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p2t1 == p2t)
	_s.add(p1t1 == p1t)
	_s.add(p1x1 == If(0 < p1t,_N1,0))
	_s.add(p1c1 == If(0 < p1t,p1c-_N1,p1c))
	_s.add(p2x1 == If((0<p2t),(_N2),0))
	_s.add(p2c1 == p2c-_N2)
	_s.add(0 <= -p1c+_N1)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),0 < p1c-_n1)))
	_s.add(Or(_N1==0,0 < p1c-_N1 + 1))
	_s.add(0 <= -p2c+_N2)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),0 < p2c-_n2)))
	_s.add(Or(_N2==0,0 < p2c -_N2 + 1))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(And(((p1t)==(p2t)),((p1c)==(p2c))))
	_s.add(Not(((If(0 < p1t,_N1,0))==(If((0<p2t),(_N2),0)))))

except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()

	sys.exit(1)

try:
	result=_s.check()
	if sat==result:
		print "Counter Example"
		print _s.model()
	elif unsat==result:
		result
		try:
			if os.path.isfile('j2llogs.logs'):
				file = open('j2llogs.logs', 'a')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
			else:
				file = open('j2llogs.logs', 'w')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
		except Exception as e:
			file = open('j2llogs.logs', 'a')
			file.write("\n**************\nProof Details\n**************\n"+"Error"+"\n")
			file.close()
		print "Successfully Proved"
	else:
		print "Failed To Prove"
except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()
