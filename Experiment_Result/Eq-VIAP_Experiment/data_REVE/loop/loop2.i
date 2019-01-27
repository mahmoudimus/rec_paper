extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int n) {
  int i = n;
  int j = 0;

  while (i >= 0) {
    i = i - 1;
    j++;
  }
  return j;
}
