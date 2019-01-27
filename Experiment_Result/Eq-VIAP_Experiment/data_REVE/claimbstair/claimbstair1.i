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

    int n;
    int result = 0;
    int prev = 1;
    int cur = 0;
    int sum;
    
    if(n<=1){
        result = 1;
    }
    else{
       sum = 2;
       for (int i = 2;i < n; i++) { 
            cur = sum;
            sum += prev;
            prev = cur;
       }
       result = sum; 
    }
    __VERIFIER_assert(1==1);
    return result;

}





