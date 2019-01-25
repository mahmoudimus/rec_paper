extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int n) {
  int j = 1;
  int x = 0;
  while (j <= n) {
    x = x + j;
    j++;
  }
  return x;
}
