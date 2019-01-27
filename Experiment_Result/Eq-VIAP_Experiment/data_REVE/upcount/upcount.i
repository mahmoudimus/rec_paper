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
  int p2n;
  int p1m = 0;
  int p2m = 0;

  __VERIFIER_assume(p1n==p2n);


     
   while((p1n >= 0)) {
      p1m++;
      p1n--;
   }
     
   while((p2n > 0)) {
      p2m++;
      p2n--;
   }
  
  __VERIFIER_assert(p1m==p2m+1);
  
  
  
  
}
