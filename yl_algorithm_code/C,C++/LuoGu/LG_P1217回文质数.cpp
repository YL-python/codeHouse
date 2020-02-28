#include <iostream>
#include <string>

using namespace std;

int a, b; 
bool ss_book[10000001];

bool make_ss(){
	ss_book[0]=ss_book[1] = 1;
	for(int i=0;i<=10000000;i++){
		if(ss_book[i]==0){
			for(int j=i+i;j<=10000000;j+=i){
				ss_book[j] = 1;
			}
		}
	}
}


bool huiwen(int x){
	int temp=x,num=0;
	while(temp){
		num = num*10 + temp %10;
		temp /= 10;
	}
	if(num == x){
		return true;
	}else{
		return false;
	}
}

void fun(int x){
	if(huiwen(x) && !ss_book[x]){
		cout << x <<endl;
	}
}

int main(){
	
	cin >>a >> b;
	//b<=10000000这个判断条件来自：除了11以外，一个数的位数是偶数的话，不可能为回文数素数。
    // 如果一个回文素数的位数是偶数，则它的奇数位上的数字和与偶数位上的数字和必然相等；
    // 根据数的整除性理论，容易判断这样的数肯定能被11整除，所以它就不可能是素数。
	if(b > 10000000){  // 玄学说  没有偶数位的回文数 
		b=9999999;
	}
	make_ss();
	for(int i=a;i<=b;i++){
		fun(i);
	}
	
	return 0;
}




























