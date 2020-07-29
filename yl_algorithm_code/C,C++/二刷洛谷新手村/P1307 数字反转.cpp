#include <iostream>
using namespace std;

string s;
int a[20],cnt,flag;

int main() {

	cin >> s;

	if(s[0] == '-') {
		cout << "-";
		flag = 1;
	}
	for(int i=0 + flag; i<s.length(); i++) {
		a[cnt++] = s[i] - '0';
	}
	flag = 0;
	for(int i=cnt-1; i>=0; i--) {
		if(a[i] == 0 && flag == 0) {
			continue;
		}
		flag = 1;
		cout << a[i];
	}

	return 0;
}
