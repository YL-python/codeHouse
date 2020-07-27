#include<iostream>
#include<string>
using namespace std;

// 定义全局变量默认初始值值是 0
// 数组下标表示0-9 存的值是 出现的次数 
int a[10];

int main() {
	string s;
	cin >> s;
	for(int i = s.length()-1; i>=0; i--) {
		a[s[i] - '0'] ++;
	}

	for(int i=0; i<10; i++) {
		if(a[i]!=0) {
			cout << i << ":" << a[i] << endl;
		}
	}
	return 0;
}








