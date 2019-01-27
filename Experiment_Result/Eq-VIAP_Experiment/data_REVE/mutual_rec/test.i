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

    int p1l,p1m;
    int p1x=1; int p1y=1;

    int p2l,p2m;
    int p2x=2; int p2y=2;


    while (__VERIFIER_nondet_int()) {
            p1l = p1x;
            p1m = p1y;
            p1x = p1l + p1m;
            p1y = p1l + p1m;
    }
 

 
    while (__VERIFIER_nondet_int()) {
            p2l = p2x;
            p2m = p2y;
            p2x = p2l + p2m;
            p2y = p2l + p2m;
    }
    p2x=p2x/2;
    p2y=p2y/2;

    __VERIFIER_assert(p1x  == p2x);
   


}






