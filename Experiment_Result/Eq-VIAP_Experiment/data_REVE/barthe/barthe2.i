extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int f(int n, int c) {
    int i = 0;
    int j = c;
    int x = 0;

    while ((i < n)) {
        x = x + j;
        j = j + 5;
        i++;
    }
    return x;
}