#include <iostream>
using namespace std;

int apple(int m,int n) {
	if(m == 0 || n == 1) {
		return 1;
	}
	if(n > m ) {
		return apple(m,m);
	}
	return apple(m-n, n) + apple(m, n-1);
}

int main() {
	int k;
	cin >> k;
	for(int i=0; i<k; i++) {
		int m,n;
		cin >> m>> n;
		cout << apple(m,n) << endl;
	}
}
/*
�������Ĺؼ��ǵ��ƺ�����

m��ƻ������n�������У���ô���庯��Ϊapple(m,n)��

1.m=0��û��ƻ������ôֻ��һ�ַŷ�����apple(0,n)=1

2.n=1��ֻ��һ�����У������л�����ƻ������ôֻ��һ�ַŷ���apple(m,1)=1

3.n>m����m��ƻ������m����������һ���ģ���apple(m,n)=apple(m,m)

4.m>=n����ʱ��Ϊ���������һ���������Ӷ���ƻ�������ǲ����������Ӷ���ƻ����
	�����������Ӷ���ƻ����������һ�����ӿ�����һ���ģ���=apple(m,n-1)��
	�������Ӷ���ƻ����Ҳ��������ÿ��������һ��ƻ����m��ƻ���е�n������n�������У�
	ʣ�µ�m-n��ƻ�������m-n��ƻ������n������������һ���ģ���=apple(m-n, n)��
	��ʱ��apple(m,n)=apple(m-n, n)+apple(m,n-1)��
https://blog.csdn.net/weixin_38505045/article/details/88366785
*/

