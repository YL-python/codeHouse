#include <iostream>
#include <string>
using namespace std;

// 快速筛除 [2,N] 之间的质数   筛出法计算质数表 

int main(){
	int num[1005];
	num[0]=0,num[1]=0;
	for(int i=2;i<1005;i++){
		num[i] = i;
	}
	for(i=2;i<1005;i++){
		if(num[i]!=0){
			for(int j=i+i;j<=1005;j+=i){  // 吧不是0的数的所有倍数去除 
				num[j] = 0;
			}
		}
	}
	
	return 0;
}

