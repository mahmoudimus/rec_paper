extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();


int climbStairs1(int n)
{

    int result = 0;
    int count1 = 1;
    int count2 = 1;
    int temp;
    
    if(n<=1){
        result = 1;
    }
    else{
       for (int i = 2;i < n; i++) { 
            temp = count2;
            count2 = temp + count1; 
            count1 = temp;
       }
       result = count2;
    }


    return result;
}





