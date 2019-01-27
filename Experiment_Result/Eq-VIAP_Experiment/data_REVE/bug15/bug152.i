extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int z) {
    int y = 0;
    int x = 1;

    while (x < 10) {

        y = 2 + x;
        x = y + y;
    }

    return x * 2;
}