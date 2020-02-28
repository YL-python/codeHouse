#include <iostream>
#include <string>
using namespace std;

string s;
int len;

void huiwen(int x){
	for(int i=0;i<=len-x;i++){
		int flag = 1;
		for(int x1 = i,x2 = i+x; x1<x2; x1++,x2--){
			if(s[x1] != s[x2]){
				flag = 0;
				break;
			}
		}
		if(flag){
			for(int k=i;k<=i+x;k++){
				cout << s[k];
			}
			cout << endl;
		}
	}
}

int main() {
	cin >> s;
	len = s.length();
	for(int i=1;i<=len;i++){
		huiwen(i);
	}
	return 0;
}
