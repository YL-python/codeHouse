#include<iostream>
#include<string>
using namespace std;
int main(){
	string s1,s2;
	getline(cin,s1);  // c++的字符串输入函数 
	getline(cin,s2);  // 第一个参数是输入流 第二个参数是保存的对象  
	int a[260];
	for(int i=0; i<s2.length(); i++){
		a[s2[i]] = 1;
	}
	
	for(int i=0;i<=s1.length();i++){
		if(a[s1[i]] == 1){
			continue;
		}else{
			cout << s1[i]; 
		}
	}
	return 0;
}
