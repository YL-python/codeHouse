#include <iostream>
using namespace std;

// ��������������ȫ�ֱ�������һ�ο�����һ��Сֵ������ 
int N=20190324;

main(){
	int mod = 10000;
	int a,b,c,ans;
	a=1,b=1,c=1; 
	for(int i=4;i<=N;i++){
		ans = (a+b+c) % mod;
		a=b,b=c,c=ans;
	}
	cout << ans << endl;
	return 0;
} 
/*
�������� 1, 1, 1, 3, 5, 9, 17, �����ӵ� 4 �ʼ��ÿ���ǰ 3 ��ĺ͡���
 �� 20190324 ������ 4 λ���֡�
*/ 
