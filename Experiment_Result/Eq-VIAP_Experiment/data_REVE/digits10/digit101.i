extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int n) {
  int result = 1;
  n = n/10;

  while (n > 0) {
    result++;
    n = n / 10;
    if (n > 0) {
      result++;
      n = n / 10;
      if (n > 0) {
        result++;
        n = n / 10;
        if (n > 0) {
          result++;
          n = n / 10;
        }
      }
    }
  }
  return result;
}