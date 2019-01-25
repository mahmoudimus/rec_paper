extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();



int main() {
    int p1n;
    int p1i = 1;
    int p1j = 0;
    int p2n;
    int p2i = 1;
    int p2j = 2;
    
    __VERIFIER_assume(p1n==p2n);
    

    if (p1n < 1) {
        p1n = 1;
    }

    while (p1i <= p1n) {
        p1j = p1j + 2;
        p1i++;
    }

    

    if (p2n < 1) {
        p2n = 1;
    }

    while (p2i < p2n) {
        p2j = p2j + 2;
        p2i++;
    }

    __VERIFIER_assert(p1j==p2j);
    

}

