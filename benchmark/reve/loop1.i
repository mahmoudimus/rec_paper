extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int n)
{

  int i = 0;
  int j = 0;

  while (i <= n) {
    i++;
    j++;
  }
  return j;
}
