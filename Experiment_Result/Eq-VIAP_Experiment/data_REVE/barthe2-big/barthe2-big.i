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
    int p1i = 1;
    int p1x = 1;

    int p2n;
    int p2i = 1;
    int p2x = 1;

  __VERIFIER_assume(p1n==p2n);


    while ( p1i <= p1n) {
        p1x = p1x * 5;
        p1i++;
    }

    p1i = 1;

    while (p1i <= p1n) {
        p1x = p1x + p1i;
        p1i++;
    }


    while ( p2i <= p2n) {
        p2x = p2x * 5;
        p2i++;
    }

    p2i = 0;

    while ( p2i <= p2n) {
        p2x = p2x + p2i;
        p2i++;
    }


  __VERIFIER_assert(p1x==p2x);
  
  
  
  
}
