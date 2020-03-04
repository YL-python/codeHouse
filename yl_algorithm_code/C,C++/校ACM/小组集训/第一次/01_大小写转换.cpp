#include <iostream>
#include <string>
using namespace std;

int main () {
	string s;
	cin >> s;
	int len = s.length();
	for(int i=0; i<len; i++) {
		if(s[i] >=65 && s[i] <= 90) {
			s[i] += 32;
		} else {
			s[i] -= 32;
		}
	}
	cout << s;
	return 0;
}
/*
问题描述
　　编写一个程序，输入一个字符串（长度不超过20），然后把这个字符串内的每一个字符进行大小写变换，
	即将大写字母变成小写，小写字母变成大写，然后把这个新的字符串输出。
　　输入格式：输入一个字符串，而且这个字符串当中只包含英文字母，不包含其他类型的字符，也没有空格。
　　输出格式：输出经过转换后的字符串。
*/
