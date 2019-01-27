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

  while((0 < c)) {
    if(0 < t) {
      x ++;
    }
    c = c - 1;
  }

  return x;
}