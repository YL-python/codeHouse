#include <iostream>
using namespace std;

int ans = 0;

void js(int x){
	while(x){
		if(x%10 == 1){
			ans++;
		}
		x/=10;
	}
}

int main (){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		js(i);
	} 
	cout << ans;
	return 0;
}
/*
����������n���жϴ�1��n֮�У�����1һ��Ҫ���ּ��Ρ�
����1123������������������1��
����15����ô��1��15֮�У�һ��������8��1��
*/
