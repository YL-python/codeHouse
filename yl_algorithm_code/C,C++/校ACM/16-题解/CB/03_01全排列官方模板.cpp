#include <iostream>
using namespace std;
int a[] = {1,2,3,4,5,6,7,8,9};
int ans;

bool test(){
	int A = a[0], b = a[1], c = a[2];
	int def = a[3] * 100 + a[4] * 10 + a[5];
	int ghi = a[6] * 100 + a[7] * 10 + a[8];
	if((b * ghi + c * def) % (c * ghi) == 0 && (b * ghi + c * def) / (c * ghi) == (10 - A)){
		return true;
	}else{
		return false;
	}
}

// �ݹ��������ȫ���У� ������û���ظ�Ԫ�ص���Ŀ 
void f(int k) {
	if(k == 9){
		if(test()){
			ans++;
		}
	}
	for(int i=k; i<9; i++) {
		{int t = a[i]; a[i] = a[k]; a[k] = t;}
		f(k+1);
		{int t = a[i]; a[i] = a[k]; a[k] = t;}
	}
}

int main () {
	f(0);
	cout << ans << endl;
	return 0;
}
/*
����ʽ

     B      DEF
A + --- + ------- = 10
     C      GHI

�������ʾ�����⣬���Բμ���ͼ1.jpg����


�����ʽ��A~I����1~9�����֣���ͬ����ĸ����ͬ�����֡�

���磺
6+8/3+952/714 ����һ�ֽⷨ��
5+3/1+972/486 ����һ�ֽⷨ��

�����ʽһ���ж����ֽⷨ��

ע�⣺���ύӦ���Ǹ���������Ҫ��д�κζ�������ݻ�˵�������֡�
*/
