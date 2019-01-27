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
  int p2n;
  int p1i = 0;
  int p1j = 0;
  int p2i = p2n;
  int p2j = 0;

  __VERIFIER_assume(p1n==p2n);


  while (p1i <= p1n) {
    p1i++;
    p1j++;
  }


  while (p2i >= 0) {
    p2i = p2i - 1;
    p2j++;
  }
  
  __VERIFIER_assert(p1j==p2j);
  
  
  
  
}
