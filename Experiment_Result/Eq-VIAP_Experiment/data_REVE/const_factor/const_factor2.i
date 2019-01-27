extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int x, int n){
  int i, k = 0;
  for (i=0; i!=n; ++i){
    x += k;
    k += 5;
    if (i >= 5)
      k += 15;
  }
  return x;
}