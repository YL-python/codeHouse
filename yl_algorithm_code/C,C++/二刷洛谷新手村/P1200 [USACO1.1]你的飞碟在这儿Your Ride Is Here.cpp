#include <iostream>
using namespace std;

int str2int(char c) {
	return c - 'A' + 1;
}


int main() {

	string s1,s2;
	cin >> s1 >> s2;
	int cnt1=1,cnt2=1;
	for(int i=0; i<s1.length(); i++) {
		cnt1 *= str2int(s1[i]);
		cnt1 %= 47;
	}
	for(int i=0; i<s2.length(); i++) {
		cnt2 *= str2int(s2[i]);
		cnt2 %= 47;
	}
	if(cnt1 == cnt2) {
		cout << "GO";
	} else {
		cout << "STAY";
	}

	return 0;
}
