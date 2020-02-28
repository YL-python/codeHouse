#include <iostream>
#include <string>
using namespace std;

string s1,s2;
int a[300];

int main(){
	getline(cin,s1);
	getline(cin,s2);
	for(int i=0;i<s1.length();i++){
		a[s1[i]]++;
	}
	for(int i=0;i<s2.length();i++){
		a[s2[i]]++;
	}
	for(int i=0;i<300;i++){
		if(a[i] == 0){
			continue;
		}else{
			for(int j=0;j<a[i];j++){
				printf("%c",i);
			}
		}
	}
	return 0;
}

