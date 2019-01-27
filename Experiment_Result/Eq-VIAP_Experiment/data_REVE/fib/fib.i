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
    int p1f = 0;   
    int p1g = 1;
    int p1h = 0;

    int p2n;
    int p2f = 1;  
    int p2g = 1;
    int p2h = 0;

  __VERIFIER_assume(p1n==p2n);




  while((p1n > 0)) {
    p1h = p1f + p1g;
    p1f = p2g;
    p1g = p1h;
    p1n --;
  }

  



  while((p2n > 0)) {
    p2h = p2f + p2g;
    p2f = p2g;
    p2g = p2h;
    p2n --;
  }


  __VERIFIER_assert(p1g==p2g);
  
  
  
  
}
