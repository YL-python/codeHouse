#include <iostream>
#include <string>
using namespace std;

/*
�������ж�
���ǻ�����������������ԭ����ӣ�ֱ���ǻ�����Ϊֹ 
*/

// �ж��ǲ��ǻ����� 
int digit[1005];
bool huiwen(int x){
	int count = 0;
	while(x){
		digit[count++] = x%10;
		x /= 10;
	}
	for(int i=0;i<count/2;i++){
		if(digit[i] != digit[count-1-i]){
			return false;
		}
	} 
	return true;
}

// ��תһ����
int rev(int x){
	int ret = 0;
	while(x){
		ret = ret*10 + x%10;
		x /= 10;
	}
	return ret;
} 


int main(){
	int n,m=0,num[1005];
	cin >> n;
	num[m++] = n;
	
	while(!huiwen(n)){
		n += rev(n);
		num[m++] = n;
	}
	
	cout << m-1 << endl;
	for(int i=0;i<m;i++){
		if(i != m-1){
			cout << num[i] << "--->";
		}else{
			cout << num[i] << endl;
		}
	}
	return 0;
}

