#include <iostream>
using namespace std;
long long ans = 0;
int a,b;

void tj(int x){
	int y;
	while(x){
		y = x%2;
		x/=2;
		if(y == 1){
			ans ++;
		}
	}
} 
int main (){
	cin >> a >> b;
	for(int i=a;i<=b;i++){
		tj(i);
	}
	cout << ans;
	return 0;
}
/*
������L,R��ͳ��[L,R]�����ڵ��������ڶ������°����ġ�1���ĸ���֮�͡�
������5�Ķ�����Ϊ101������2����1����
*/
