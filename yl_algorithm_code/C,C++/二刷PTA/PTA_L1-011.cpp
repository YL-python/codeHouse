#include <iostream>
#include <string>
using namespace std;

int a[260];

int main() {
	string s1,s2;
	getline(cin,s1);  // c++���ַ������뺯�� 
	getline(cin,s2);  // ��һ�������������� �ڶ��������Ǳ���Ķ���  
		
	for(int i = 0;i<s2.length();i++){
		a[s2[i]] = 1;  // ��ǳ��ֹ����ַ� 
	}
	for(int i = 0;i<s1.length();i++){  // ʱ�临�Ӷ� On 
		if(a[s1[i]]){  // ���ֹ���ֱ���˳�����ӡ 
			continue;
		}else{
			cout << s1[i]; 
		}
	}
	return 0;
}
