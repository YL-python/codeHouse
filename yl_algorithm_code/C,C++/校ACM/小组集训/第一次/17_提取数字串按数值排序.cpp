#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isnum(char c) {
	int a = c - '0';
	return a>=0&&a<=9 ? true : false;
}

int main () {
	string s;
	int a[300]; // 装数字
	int cnt = 0; // 下标
	cin >> s;

	for(int i=0; i<s.length(); i++) {
		if(isnum(s[i])){
			int anum = 0;
			while(isnum(s[i])){
				anum = anum * 10 + (s[i] - '0');
				i++;
			}
			a[cnt++] = anum; 
		}
	}

	sort(a,a+cnt);
	if(cnt == 0) {
		cout << 0;
	} else {
		for(int i=0; i<cnt; i++) {
			if(i == cnt-1) {
				cout << a[i];
			} else {
				cout << a[i] << ",";
			}
		}
	}
	return 0;
}
/*

*/
