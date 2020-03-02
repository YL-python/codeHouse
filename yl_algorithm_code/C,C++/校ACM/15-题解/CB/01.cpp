#include <iostream>
#include <sstream>
#include <string>
using namespace std;

// �ж���û�� 4
bool not4(int x) {
	int y;
	while(x) {
		y = x%10;
		if(y == 4) {
			return false;
		}
		x/=10;
	}
	return true;
}

void i2s(int num, string &str){
	stringstream ss;
	ss << num;
	ss >> str;
}

int main() {
	int ans = 0;
	for(int i=10000; i<=99999; i++) {
		if(not4(i)) {
			ans++;
		}
	}
	cout << ans << endl;
	// ---------------------------------------
	int ans2=0;
	for(int i=10000; i<=99999; i++) {
		string s ;
		i2s(i,s);
		if(s.find('4') == string::npos) {
			ans2++;
		}
	}
	cout << ans2 << endl;
	return 0;
}

/*
��ȯ��Ŀ
��Щ�˺��������֣������ ��4�������֣���Ϊ�� ������г�����;��ò�������
��Ȼ��Щ˵�������޻�̸֮������ʱ��Ҫӭ�ϴ��ڵ�����ĳ�齱��Ľ�ȯ
������
5λ����10000-99999����
Ҫ�����в�Ҫ���ִ���4���ĺ��룬
���쵥λ�������һ�£�����κ�
���Ž�ȯ���غţ����ɷ�����ȯ�����š�

���ύ�����֣�һ������������Ҫд�κζ�������ݻ�˵�������֡�
*/

