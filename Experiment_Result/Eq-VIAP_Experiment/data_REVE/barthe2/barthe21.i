extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

/*
Taken from:
  Relational verification using product programs
  Gilles Barthe, Juan Manuel Crespo, and Cesar Kunz
  IMDEA Software, Madrid, Spain
  FM 2011
  Page 4
*/

int f(int n) {
  int i = 0;
  int x = 0;
  while (i <= n) {
    x = x + i;
    i++;
  }
  return x;
}