extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int t, int c) {
  int x = 0;

  if (0 < t) {
      while((0 < c)) {
          x++;
          c--;
      }
  } else {
      while((0 < c)) {
          x--;
          c--;
      }
  }

  return x;
}