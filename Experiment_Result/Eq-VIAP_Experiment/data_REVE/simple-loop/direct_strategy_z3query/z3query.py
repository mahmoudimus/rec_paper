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
	p2z1=Int('p2z1')
	_N1=Const('_N1',IntSort())
	_N2=Const('_N2',IntSort())
	p1i1=Int('p1i1')
	_n2=Int('_n2')
	p2i1=Int('p2i1')
	p1z=Int('p1z')
	_n1=Int('_n1')
	p1z1=Int('p1z1')
	p2z=Int('p2z')
	main=Int('main')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(p1z1 == p1z)
	_s.add(p2z1 == p2z)
	_s.add(p1i1 == _N1)
	_s.add(p2i1 == _N2 + 1)
	_s.add(_N1 > 10)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),_f(_n1) <= 10)))
	_s.add(Or(_N1==0,_N1 - 1 <= 10))
	_s.add(_N2 + 1 > 10)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) + 1 <= 10)))
	_s.add(Or(_N2==0,_N2 <= 10))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((p1z)==(p2z)))
	_s.add(Not(((_N1)==(_N2 + 1))))

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
