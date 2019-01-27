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

  int p1t;
  int p1c; 
  int p1r;
  int p1x = 0;
  
  int p2t;
  int p2c; 
  int p2r;
  int p2x = 0;


  __VERIFIER_assume(p1t==p2t&&p1c==p2c&&p1r==p2r);

  if (0 < p1t) {
  
      while((0 < p1c)) {
          p1x++;
          p1c--;
      }
  } else {

  }

  while((p1r > 0)) {
      p1x+=2;
      p1r--;
  }



  

  while((0 < p2c)) {
      if (0 < p2t) {
          p2x++;
      }
      p2c--;
  }

  while((p2r > 0)) {
  
      p2x+=2;
      p2r--;
  }




  
  __VERIFIER_assert(p1x==p2x);
  
  
  
  
}
