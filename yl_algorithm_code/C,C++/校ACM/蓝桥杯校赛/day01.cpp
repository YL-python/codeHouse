#include <iostream>
#include <string>
using namespace std;

// ���ʱ�ʾ ������ �����Լ����1 
 
int a[19000];
int n=19000,count=0;

int gcd(int a,int b){
	return b?gcd(b,b%a):a;
} 

int main(){
	for(int i=1;i<=n;i++){
		if(gcd(i,n) == 1){
			count++;
//			cout << i<<endl; 
		}
	}
	printf("%d\n",count);
	return 0;
}

