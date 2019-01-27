extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int n) {
    int i = 1;
    int x = 1;

    while (__mark(1) & i <= n) {
        x = x * 5;
        i++;
    }

    i = 0;

    while (__mark(2) & i <= n) {
        x = x + i;
        i++;
    }
    return x;
}
