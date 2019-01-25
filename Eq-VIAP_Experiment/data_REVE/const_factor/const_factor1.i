extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

/* This example is taken verbatim from:
 * Rahul Sharma, Eric Schkufza, Berkeley Churchill and Alex Aiken.
 *    Data-Driven Equivalence Checking
 * OOPSLA 2013
 */

/*@ opt -infer-marks @*/

int f(int x, int n) {
  int i, k = 0;
  for (i=0; i!=n; ++i) {
    x += k*5;
    k += 1;
    if (i >= 5)
      k += 3;
  }
  return x;
}