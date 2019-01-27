extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int fib(int n) {
  int f = 1;  //  <---- starting at 1
  int g = 1;
  int h = 0;

  while(__mark(42) & (n > 0)) {
    h = f + g;
    f = g;
    g = h;
    n --;
  }

  return g;
}
