#include <iostream>
#include <sstream>
#include <string>
using namespace std;

void i2s(int num, string &str){
	// 申请一个字符流 需要 sstream库 
	stringstream ss;
	ss << num;
	ss >> str;
}

int main(){
	int i = 123;
	string s;
	i2s(i,s);
	// 找到会返回对于下标 
	cout << s.find("4") << endl;
	cout << s.find("1") << endl;
	
	// string::npos 表示不存在 
	cout << string::npos << endl;
	return 0;
}
