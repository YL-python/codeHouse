#include<iostream>
#include<string>
using namespace std;

// ����ȫ�ֱ���Ĭ�ϳ�ʼֵֵ�� 0
// �����±��ʾ0-9 ���ֵ�� ���ֵĴ��� 
int a[10];

int main() {
	string s;
	cin >> s;
	for(int i = s.length()-1; i>=0; i--) {
		a[s[i] - '0'] ++;
	}

	for(int i=0; i<10; i++) {
		if(a[i]!=0) {
			cout << i << ":" << a[i] << endl;
		}
	}
	return 0;
}








