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
    int p1result = 0;
    int p1prev = 1;
    int p1cur = 0;
    int p1sum;
    
    int p2n;
    int p2result = 0;
    int p2count1 = 1;
    int p2count2 = 1;
    int p2temp;

    
    
    __VERIFIER_assume(p1n==p2n);
    
    if(p1n<=1){
        p1result = 1;
    }
    else{
       p1sum = 2;
       for (int p1i = 2;p1i < p1n; p1i++) { 
            p1cur = p1sum;
            p1sum += p1prev;
            p1prev = p1cur;
       }
       p1result = p1sum; 
    }

    
    if(p2n<=1){
        p2result = 1;
    }
    else{
       for (int p2i = 2;p2i < p2n; p2i++) { 
            p2temp = p2count2;
            p2count2 = p2temp + p2count1; 
            p2count1 = p2temp;
       }
       p2result = p2count2;
    }


     __VERIFIER_assert(p1result==p2result);


}





