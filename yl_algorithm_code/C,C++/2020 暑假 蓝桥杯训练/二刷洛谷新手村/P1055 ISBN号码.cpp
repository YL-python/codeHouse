#include <iostream>
#include <cstring>
using namespace std;

int temp=0;
string s;

int main() {

	cin >> s;
	temp += (s[0]-'0') * 1;
	temp += (s[2]-'0') * 2;
	temp += (s[3]-'0') * 3;
	temp += (s[4]-'0') * 4;
	temp += (s[6]-'0') * 5;
	temp += (s[7]-'0') * 6;
	temp += (s[8]-'0') * 7;
	temp += (s[9]-'0') * 8;
	temp += (s[10]-'0') * 9;
	temp %= 11;
	if(temp == 10) {
		temp = 'X';
	} else {
		temp += '0';
	}
	if(temp == s[12]) {
		cout << "Right";
	} else {
		s[12] = temp;
		cout << s;
	}

	return 0;
}
