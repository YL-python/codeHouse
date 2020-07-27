#include <iostream>
#include <string>
using namespace std;

string numStr[11] =  {"ling","yi","er","san","si","wu","liu","qi","ba","jiu","fu"};
string s;

int main() {
	cin >> s;
	int len = s.length();
	int start = 0;
	if(s[0]=='-') {
		cout << numStr[10] << " ";
		start = 1;
	}
	for(int i=start; i<len-1; i++) {
		cout << numStr[s[i]-'0'] << " ";
	}
	cout << numStr[s[len-1]-'0'];
	return 0;
}
