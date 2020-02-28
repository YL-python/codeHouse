#include <iostream>
using namespace std;

// �������ţ�ֱ�ӱ���
// ϸ�ھ��� ��ôȥ��

// ����2 �� 4 �����ֶ�Ӧ�� vis�����ֵ��0
int vis[2500];

bool have2or4(int x) {
	while(x) {
		if(x%10 == 2 || x%10 == 4) {
			return true;
		}
		x/=10;
	}
	return false;
}

void init() {
	for(int i=0; i<=2500; i++) {
		if(have2or4(i)) {
			vis[i] = 1;
		}
	}
}


main() {
	int ans = 0; 
	init();
	for(int i=1; i<=2019; i++) {
		// j = i+1 ȥ�� 
		for(int j=i+1; j<=2019; j++) {
			for(int k=j+1; k<=2019; k++) {
				if(!vis[i] && !vis[j] && !vis[k] && i+j+k==2019){
					ans++;
				}
			}
		}
	}
	cout << ans;
	return 0;
}
/*
 �� 2019 �ֽ�� 3 ��������ͬ��������֮�ͣ�����Ҫ��ÿ��������������
 ������ 2 �� 4��һ���ж����ֲ�ͬ�ķֽⷽ����
 ע�⽻�� 3 ��������˳����Ϊͬһ�ַ��������� 1000+1001+18 ��
 1001+1000+18 ����Ϊͬһ�֡�
*/
