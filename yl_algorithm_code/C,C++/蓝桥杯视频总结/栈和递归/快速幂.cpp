#include <iostream>
#include <string>
using namespace std;

long long x, y, p; 

long long f(long long x,long long y, long long p){
	if(y == 0){
		return 1%p;
	}else if(y & 1){
		long long temp = f(x, y/2, p);
		return temp * temp % p * x % p;
	} else{
		long long temp = f(x, y/2, p);
		return temp * temp % p;
	}
}

/*
+ - 一般使用2个CPU时钟
位运算 只要 1 个
* 要 4 个
/ 要 40 个

x & 1  奇数返回 1  偶数返回 0 
*/ 

int main(){
	int n;
	scanf("%I64d",&n);
	while(t--){
		scanf("%I64d%I64d%I64d",&x,&y,&p);
		printf("%I64d\n",f(x,y,p));
	}
//	for(int i=0;i<n;i++){
//		scanf("%I64d%I64d%I64d",&x,&y,&p);
//		printf("%I64d\n",f(x,y,p));
//	}
	
	return 0;
}
/*
求 x 的 y 次方对 p 取余 
1
2 10 10000

1024
*/  



























