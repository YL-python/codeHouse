#include <iostream>
#include <sstream>
#include <string>
using namespace std;

void i2s(int num, string &str){
	// ����һ���ַ��� ��Ҫ sstream�� 
	stringstream ss;
	ss << num;
	ss >> str;
}

int main(){
	int i = 123;
	string s;
	i2s(i,s);
	// �ҵ��᷵�ض����±� 
	cout << s.find("4") << endl;
	cout << s.find("1") << endl;
	
	// string::npos ��ʾ������ 
	cout << string::npos << endl;
	return 0;
}
