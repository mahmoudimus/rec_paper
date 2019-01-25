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

    int p1x;
    int p1i = 0;

    int p2x;
    int p2i = 10;

  __VERIFIER_assume(p1x==p2x);

    
    while ((p1i <= 10)) {
        if (p1i == p1x) {
            break;
        }
        p1i++;
    }
  
 
    while ((p2i >= 0)) {
        if (p2i == (10 - p2x)) {
            break;
        }
        p2i--;
    }


  __VERIFIER_assert(p1i==10 - p2i);
  
  
  
  
}
