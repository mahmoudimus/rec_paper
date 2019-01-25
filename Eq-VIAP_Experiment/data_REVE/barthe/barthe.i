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

    int p1n; 
    int p1c;
    int p1i = 0;
    int p1j = 0;
    int p1x = 0;

    int p2n;
    int p2c;
    int p2i = 0;
    int p2j = p2c;
    int p2x = 0;

  __VERIFIER_assume(p1n==p2n&&p1c==p2c);

    while ((p1i < p1n)) {

        p1j = 5 * p1i + p1c;
        p1x = p1x + p1j;
        p1i++;
    }




    while ((p2i < p2n)) {
        p2x = p2x + p2j;
        p2j = p2j + 5;
        p2i++;
    }


  __VERIFIER_assert(p1x==p2x);
  
  
  
  
}
