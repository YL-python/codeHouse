#include<iostream>
#include<string>
using namespace std;

string s;
int numG,numP,numL,numT;

int main() {
	getline(cin,s);
	int len = s.length();
	for(int i=0; i<len; i++) {
		if(s[i]=='G'||s[i]=='g') {
			numG++;
		}
		if(s[i]=='P'||s[i]=='p') {
			numP++;
		}
		if(s[i]=='L'||s[i]=='l') {
			numL++;
		}
		if(s[i]=='T'||s[i]=='t') {
			numT++;
		}
	}
	while(numG!=0||numP!=0||numL!=0||numT!=0) {
		if(numG!=0) {
			cout << "G";
			numG--;
		}
		if(numP!=0) {
			cout << "P";
			numP--;
		}
		if(numL!=0) {
			cout << "L";
			numL--;
		}
		if(numT!=0) {
			cout << "T";
			numT--;
		}
	}

	return 0;
}
