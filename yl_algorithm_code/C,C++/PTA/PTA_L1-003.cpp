#include<iostream>
#include<string>
using namespace std;
string s;
int l,m[10];
int main(){
	cin >> s;
	l = s.length();
	for(int i=0;i<l;i++){
		m[s[i]-'0']++;
	}
	for(int i=0;i<10;i++){
		if(m[i]!=0){
			cout << i << ":" << m[i] << endl; 
		}
	}
	return 0;
}
