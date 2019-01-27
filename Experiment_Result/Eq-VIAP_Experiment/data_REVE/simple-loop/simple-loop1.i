extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();


int f(int z) {
  int i = 0;

  while (i <= 10) {
    i++;
  }
  return i;
}
