extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();


int nested_while1(int x,int g)
{

    int i = 0;
    int x;
    int g;

    while (i < x) {
        i = i + 1;
        g = g - 1;
        while (x < i) {
            x = x + 1;
            g = g + 1;
        }
    }
    return g;
}





