#include <iostream>
using namespace std;

long long a;

int main () {
	cin >> a;
	if(a <= 2) {
		cout << a;
	} else {  // ����2 
		if(a%2 == 1) { // ���� 
			cout << a * (a-1) * (a-2);
		}else{  // ż�� 
			if(a % 3 == 0){
				cout << (a-1) * (a-2) * (a-3);
			} else{
				cout << a * (a-1) * (a-3);
			}
		}
	}
	return 0;
}
/*
��֪һ��������N���ʴ�1~N����ѡ�������������ǵ���С������������Ϊ���١�
���� n3  ���ݷ�Χ10 6  ��ʱ��
���Խ����Խ�� 
*/
