#include <iostream>
#include <string>
using namespace std;

// ��ͳ�����ж� 
bool ss(int a){
    for(int i=2;i*i<=a;i++)
        if(a%i==0)
            return false;
    return true;
}

int main(){
	int num[1005];
	num[0]=0,num[1]=0;
	for(int i=2;i<1005;i++){
		num[i] = i;
	}
	
	// ����ɸ�� [2,N] ֮�������   ɸ�������������� 
	for(i=2;i<1005;i++){
		if(num[i]!=0){
			// �ɲ���0���������б���ȥ�� 
			for(int j=i+i;j<=1005;j+=i){ 
				num[j] = 0;
			}
		}
	}
	
	return 0;
}

