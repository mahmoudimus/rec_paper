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
    int p1result = 1;
    
    int p2n;
    int p2result = 1;
    int p2b = 1;
    int p2retval = -1;

  __VERIFIER_assume(p1n==p2n);


   p1n = p1n/10;



  while (p1n > 0) {
    p1result++;
    p1n = p1n / 10;
    if (p1n > 0) {
      p1result++;
      p1n = p1n / 10;
      if (p1n > 0) {
        p1result++;
        p1n = p1n / 10;
        if (p1n > 0) {
          p1result++;
          p1n = p1n / 10;
        }
      }
    }
  }

  



    while (!(p2b == 0)) {
        if (p2n < 10) {
            p2retval = p2result;
            p2b = 0;
        } else if (p2n < 100) {
            p2retval = p2result + 1;
            p2b = 0;
        } else if (p2n < 1000) {
            p2retval = p2result + 2;
            p2b = 0;
        } else if (p2n < 10000) {
            p2retval = p2result + 3;
            p2b = 0;
        } else {
            p2n = p2n / 10000;
            p2result = p2result + 4;
        }
    }
  
  
  

  __VERIFIER_assert(p1result==p2retval);
  
  
  
  
}
