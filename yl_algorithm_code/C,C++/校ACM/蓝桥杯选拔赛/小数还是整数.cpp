#include <iostream>
#include <string>
using namespace std;

string s; 

int main(){
	getline(cin,s);
	int len = s.length();
	int flag = 0;
	for(int i=0;i<len;i++){
		if(s[i] == '.'){
			flag=1;
		}
	}
	if(!flag){
		cout << "����"; 
	}else{
		cout << "С��"; 
	} 
	return 0;
}
/*
Description

����һ���������ж���С������������һ���ǺϷ������֣�



Input
һ�����֣�С��1000



Output
�����С�������'С��'����������������'����'


Sample Input 1 

1.3
Sample Output 1

С��
Sample Input 2 

5
Sample Output 2

����
Sample Input 3 

3.0
Sample Output 3

С��
*/
