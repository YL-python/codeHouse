#include <iostream>
using namespace std;

int N,n,m;

int main() {
	cin >> N;
	// ��N����һ����,����һ�����ֵ��ca
	int temp=0,chen = 0,ca = 0;
	for(int i=1; i<=1000000; i++) {
		temp += i;
		if(temp >= N) {
			chen = i;
			ca = temp - N;
			break;
		}
	}
//	cout << chen << " " << ca << endl;
	// chen  �������ˣ���Ҫ�ж��������㻹���½���
	if(chen % 2) {  // ������
		cout << 1+ca << "/" << chen-ca;
	} else {  // �½���
		cout << chen-ca << "/" << 1+ca;
	}
	return 0;
}
