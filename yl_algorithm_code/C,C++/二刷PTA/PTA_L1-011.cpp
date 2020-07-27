#include <iostream>
#include <string>
using namespace std;

int a[260];

int main() {
	string s1,s2;
	getline(cin,s1);  // c++的字符串输入函数 
	getline(cin,s2);  // 第一个参数是输入流 第二个参数是保存的对象  
		
	for(int i = 0;i<s2.length();i++){
		a[s2[i]] = 1;  // 标记出现过的字符 
	}
	for(int i = 0;i<s1.length();i++){  // 时间复杂度 On 
		if(a[s1[i]]){  // 出现过就直接退出不打印 
			continue;
		}else{
			cout << s1[i]; 
		}
	}
	return 0;
}
