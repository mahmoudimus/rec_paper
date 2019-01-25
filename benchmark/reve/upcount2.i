extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int upcount(int n) {
   int m = 0;
   while((n > 0)) {
      m++;
      n--;
   }
   return m+1;
}