#include <iostream>
#include <string>
using namespace std;

// ����ɸ�� [2,N] ֮�������   ɸ�������������� 

int main(){
	int num[1005];
	num[0]=0,num[1]=0;
	for(int i=2;i<1005;i++){
		num[i] = i;
	}
	for(i=2;i<1005;i++){
		if(num[i]!=0){
			for(int j=i+i;j<=1005;j+=i){  // �ɲ���0���������б���ȥ�� 
				num[j] = 0;
			}
		}
	}
	
	return 0;
}

