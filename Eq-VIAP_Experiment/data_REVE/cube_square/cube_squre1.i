extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int g(int n)
{
  int r=0;
  int i=n;

  while (__mark(0) & (i > 0)) {
    r = r + n;
    i--;
  }

  i=n;
  n=r;
  r=0;

  while (__mark(1) & (i > 0)) {
    r = r + n;
    i--;
  }

  return r;
}
