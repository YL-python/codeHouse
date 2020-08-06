#include<iostream>
#include<string>
using namespace std;

string tel;
int arr[10], index[11];

/* ��������
arr ���飺 �±��� ��ʾ0-9���֣�ֵ�����������û���ڵ绰�����������
index ���飺 �±���0-9��ֵ�� ��������� arr������±�
*/

int main() {
	cin >> tel;
	for(int i=0; i<tel.length(); i++) {
		arr[tel[i] - '0'] = 1;  // ��ǰ�绰��������˱� 1
	}

	int cnt = 0;
	for(int i=tel.length()-1; i>=0; i--) {  // ����
		if(arr[i]) {
			index[i] = cnt++;  // i���������arr���ŵ� cnt λ
		}
	}

	cout << "int[] arr = new int[]{";
	int temp = 1;  // temp����Ƿ�Ҫ��� , ����
	for(int i=tel.length()-1; i>=0; i--) {
		if(arr[i]) {
			if(temp) {
				temp = 0;
			} else {
				cout<< ',';
			}
			cout << i;
		}
	}
	cout << "};" << endl;

	cout << "int[] index = new int[]{";
	temp = 1;
	for(int i=0; i<tel.length(); i++) {
		if(temp) {
			temp = 0;
		} else {
			cout<<',';
		}
		cout << index[tel[i] - '0'];
	}
	cout << "};" << endl;
	return 0;
}
