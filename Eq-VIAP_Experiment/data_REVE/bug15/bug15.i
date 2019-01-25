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

    int p1z;
    int p1y = 0;
    int p1x = 1;

    int p2z;
    int p2y = 0;
    int p2x = 1;


  __VERIFIER_assume(p1z==p2z);



    while (p1x < 10) {
        p1y = 2 + p1x;
        p1x = p1y + p1y;
    }

  
 


    while (p2x <= 9) {
        p2y = p2x + 2;
        p2x = 2 * p2y;
    }

  __VERIFIER_assert(p1x * 2==2 * p2x);
  
  
  
  
}
