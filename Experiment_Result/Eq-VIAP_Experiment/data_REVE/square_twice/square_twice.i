extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int main()
{

    int p1n;
    int p1r=0;
    int p1i=p1n;
  
    int p2n;
    int p2r=0;
    int p2i=p2n;

  __VERIFIER_assume(p1n==p2n);


  while ((p1i > 0)) {
    p1r = p1r + p1n;
    p1i--;
  }

  p1i=p1n;
  p1n=p1r;
  p1r=0;

  while ((p1i > 0)) {
    p1r = p1r + p1n;
    p1i--;
  }

  

  while ((p2i > 0)) {
    p2r = p2r + p2n;
    p2i--;
  }


  __VERIFIER_assert(p1r==p2r);
  
  
  
  
}
