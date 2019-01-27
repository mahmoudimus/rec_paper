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
    int p1i = 0;
    int p1x = 0;

    int p2n;
    int p2j = 1;
    int p2x = 0;

  __VERIFIER_assume(p1n==p2n);


  while (p1i <= p1n) {
    p1x = p1x + p1i;
    p1i++;
  }
  

  while (p2j <= p2n) {
    p2x = p2x + p2j;
    p2j++;
  }

  __VERIFIER_assert(p1x==p2x);
  
  
  
  
}
