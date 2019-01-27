extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int z) {
    int x = 1;
    int y = 0;

    while (x <= 9) {
        __mark(42);
        y = x + 2;
        x = 2 * y;
    }

    return 2 * x;
}