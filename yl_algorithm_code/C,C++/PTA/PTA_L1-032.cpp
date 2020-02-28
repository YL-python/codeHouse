#include<iostream>
#include<string>
using namespace std;

int main(){
	int n;
	char c;
	string s1;
	string str;
	cin >> n >> c;
	getchar();
	getline(cin,str);
	
	int len = str.length();
	if(n>len){
		for(int i=0;i<n-len;i++){
			cout << c;
		}
		int k=0;
		for(int i=n-len;i<n;i++){
			cout <<str[k];
			k++;
		}
	}else{
		for(int i=len-n;i<len;i++){
			printf("%c",str[i]);
		}
	}
	
	return 0;
}

