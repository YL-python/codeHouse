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
+ - һ��ʹ��2��CPUʱ��
λ���� ֻҪ 1 ��
* Ҫ 4 ��
/ Ҫ 40 ��

x & 1  �������� 1  ż������ 0 
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
�� x �� y �η��� p ȡ�� 
1
2 10 10000

1024
*/  



























