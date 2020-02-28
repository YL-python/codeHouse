#include <iostream>
#include <string>
using namespace std;

int main(){
	int n;
	string s[15];
	cin >> n;
	getchar();
	for(int i=0;i<n;i++){
		getline(cin,s[i]);
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<s[i].length();j++){
			printf("%c",s[i][j]-32);
		}
		cout << endl;
	}
	return 0;
}
