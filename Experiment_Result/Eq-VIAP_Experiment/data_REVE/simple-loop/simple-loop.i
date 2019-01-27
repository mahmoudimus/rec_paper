extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();



int main() {
 
  int p1z;
  int p1i = 0;
  int p2z;
  int p2i = 1;
  
 __VERIFIER_assume(p1z==p2z);

  while (p1i <= 10) {
    p1i++;
  }

    
  while (p2i <= 10) {
    p2i++;
  }
  
 __VERIFIER_assert(p1i==p2i);
    

}

