#include<iostream>
#include<string>
using namespace std;

// ��һ���ַ��������ַ���ת�����֣�����ת�ķ��� 0
// ��Ŀ���� AB�ķ�Χ��   [1,1000]
int str2int(string s) {
	int len = s.length();
	int num = 0;
	for(int i=0; i<len; i++) {
		if(s[i] >= '0' && s[i] <= '9') {
			num*=10;
			num += s[i] - '0';
		} else {
			return 0;
		}
	}
	if(num > 1000){
		return 0;
	}else{
		return num;
	}
}

int main() {

	string stra, strb;
	int numa, numb;

	// �������������
	// �����ַ����Ե�һ���ո�ָ� �ڶ����ַ������пո�
	// 123 123 a   ������ B�� 123 a  
	cin >> stra;
	getchar();  // �Ե���һ���ո� 
	getline(cin,strb);
	
	// ���Կո�Ļ�  strb[0]�ǿո� 
	// cout << strb[0] << endl << strb.length() << endl; 

	numa = str2int(stra);
	numb = str2int(strb);

	int flag = 0;
	if(numa == 0) {
		cout << "?";
		flag = 1;
	} else {
		cout << numa;
	}
	cout << " + ";
	if(numb == 0) {
		cout << "?";
		flag = 1;
	} else {
		cout << numb;
	}
	cout << " = ";
	if(flag) {
		cout << "?";
	} else {
		cout << numa+numb;
	}
	return 0;
}
