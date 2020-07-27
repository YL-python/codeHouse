#include <iostream>
using namespace std;

int n,len;
char c;
string s;

int main() {
	cin >> n >> c;
	getchar();
	getline(cin,s);
	len = s.length();

	if(n>len) {
		for(int i=0; i< n-len; i++) {
			cout << c;
		}
		cout << s;
	} else {
		for(int i=len-n; i<len; i++) {
			cout << s[i];
		}
	}
	return 0;
}
