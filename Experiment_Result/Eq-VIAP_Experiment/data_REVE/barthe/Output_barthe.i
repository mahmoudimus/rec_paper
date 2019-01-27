Program Body
{
  int _1_ASSUME;
  _1_ASSUME = 0;
  int _1_PROVE = 0;
  int p1n;
  int p1c;
  int p1i;
  p1i = 0;
  int p1j;
  p1j = 0;
  int p1x;
  p1x = 0;
  int p2n;
  int p2c;
  int p2i;
  p2i = 0;
  int p2j;
  p2j = p2c;
  int p2x;
  p2x = 0;
  _1_ASSUME = (p1n == p2n) && (p1c == p2c);
  while (p1i < p1n)
  {
    p1j = (5 * p1i) + p1c;
    p1x = p1x + p1j;
    p1i = p1i + 1;
  }

  while (p2i < p2n)
  {
    p2x = p2x + p2j;
    p2j = p2j + 5;
    p2i = p2i + 1;
  }

  _1_PROVE = p1x == p2x;
}

Function Name:
main
Return Type:
int
Input Variables:
{}
Local Variables:
{ p1c:int p2c:int p1i:int p1j:int _1_PROVE:int p2i:int p1n:int p2j:int p1x:int p2n:int _1_ASSUME:int p2x:int}

Output in normal notation:
1. Frame axioms:
p1c1 = p1c
p2n1 = p2n
p1n1 = p1n
p2c1 = p2c

2. Output equations:
p1i1 = (_N1+0)
p1j1 = p1j3(_N1)
p2i1 = (_N2+0)
p2j1 = ((5*_N2)+p2c)
p1x1 = (((((((2*_N1)*p1c)+((10*_N1)*0))-(5*_N1))+(2*0))+(5*(_N1**2)))/2)
p2x1 = ((((((2*_N2)*p2c)-(5*_N2))+(2*0))+(5*(_N2**2)))/2)

3. Other axioms:
p1j3((_n1+1)) = ((5*(_n1+0))+p1c)
p1j3(0) = 0
(_N1>=(-(0)+p1n))
(_n1<_N1) -> ((_n1+0)<p1n)
(_N2>=(-(0)+p2n))
(_n2<_N2) -> ((_n2+0)<p2n)

4. Assumption :
((p1n==p2n) and (p1c==p2c))

5. Assertion :
((((((((2*_N1)*p1c)+((10*_N1)*0))-(5*_N1))+(2*0))+(5*(_N1**2)))/2)==((((((2*_N2)*p2c)-(5*_N2))+(2*0))+(5*(_N2**2)))/2))




Successfully Proved Assertion

Programs are Equivalent
