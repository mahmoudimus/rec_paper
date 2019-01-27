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

   int p1i = 0;
   int p1x;
   int p1g;
   int p2i = 0;
   int p2x;
   int p2g;
   
   __VERIFIER_assume(p1x==p2x&&p1g==p2g);

    while (p1i < p1x) {
        p1i = p1i + 1;
        p1g = p1g - 2;
        p1g = p1g + 1;
        while (p1x < p1i) {
            p1x = p1x + 2;
            p1x = p1x - 1;
            p1g = p1g + 1;
        }
    }
    while (p2i < p2x) {
        p2i = p2i + 1;
        p2g = p2g - 2;
        p2g = p2g + 1;
        while (p2x < p2i) {
            p2x = p2x + 2;
            p2x = p2x - 1;
            p2g = p2g + 1;
        }
    }

    
    __VERIFIER_assert(p1x==p2x);
 
}
