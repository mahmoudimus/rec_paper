extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();



int main() {
 
 
  int p1t; 
  int p1c;
  int p1x = 0;
  
  int p2t; 
  int p2c;
  int p2x = 0;
  
  __VERIFIER_assume(p1t==p2t && p1c==p2c);

  if (0 < p1t) {
      while((0 < p1c)) {
          p1x++;
          p1c--;
      }
  } else {
      while((0 < p1c)) {
          p1x--;
          p1c--;
      }
  }

  


  if (0 < p2t) {
      while((0 < p2c)) {
          p2x++;
          p2c--;
      }
  } else {
      while((0 < p2c)) {
          p2x--;
          p2c--;
      }
  }

    __VERIFIER_assert(p1x==p2x);
    

}

