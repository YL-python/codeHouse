#include <iostream>
#include <string>
#include <set>
using namespace std;

set<string> ss;


// string ������ length() �� size()û������ 
// char [] �������� 
int main(){
	int n,op;
	string str; 
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> op >> str;
		for(int j=0;j,str.size();j++){  
			if(str[j]>='A' && str[j]<='Z'){
				str[j] = 'a' + str[j] - 'A';
			}
		}
		if(op == 0){
			ss.insert(str);
		}else if(op == 1){
			if(ss.count(str)){
				cout << "YES" << endl;
			}else{
				cout << "NO" << endl;
			}
		}
	}
	return 0;
}
/*
�����������ַ���
0��ʾѧ����
1��ʾ������᲻��
����1 ���жϻ᲻�Ტ���
�����ִ�Сд 
*/

