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

    int p1x; 
    int p1n;
    int p1i, p1k = 0;

    int p2x; 
    int p2n;
    int p2i, p2k = 0;

  __VERIFIER_assume(p1x==p2x&&p1n==p2n);



  for (p1i=0; p1i!=p1n; ++p1i) {
    p1x += p1k*5;
    p1k += 1;
    if (p1i >= 5)
      p1k += 3;
  }

  

  for (p2i=0; p2i!=p2n; ++p2i){
    p2x += p2k;
    p2k += 5;
    if (p2i >= 5)
      p2k += 15;
  }

  
  
  
  
  

  __VERIFIER_assert(p1x==p2x);
  
  
  
  
}
