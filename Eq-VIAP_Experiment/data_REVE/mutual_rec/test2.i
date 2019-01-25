extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int main()
{

    int l,m;
    int x=2; int y=2;

    while (__VERIFIER_nondet_int()) {
            l = x;
            m = y;
            x = l + m;
            y = l + m;
    }
    x=x/2;
    y=y/2;

}






