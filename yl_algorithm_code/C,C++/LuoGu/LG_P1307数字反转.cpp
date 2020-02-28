#include <iostream>
#include <string>

using namespace std;

string s; 

void fzzs(string m,int x){
	int num = 0;
	for(int i=x-1;i>=0;i--){
		num*=10;
		num += (s[i]-'0');
	}
	cout << num;
}

void fzfs(string m,int x){
	int num = 0;
	for(int i=x-1;i>=1;i--){
		num*=10;
		num += (s[i]-'0');
	}
	cout << num;
}

int main(){
	getline(cin,s);
	int len = s.length();
	
	if(s[0] == '-'){
		cout << "-";
		fzfs(s,len);
	}else{
		fzzs(s,len);
	}
	
	return 0;
}




























