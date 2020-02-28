#include <iostream>
#include <string>
using namespace std;

int main(){
	string str1;
	getline(cin,str1);
	char a[5] = {'a','e','i','o','u'};
	
	int temp=0,len = str1.length();
	
	for(int i=0;i<len;i++){
		if(temp == 1){
			break;
		}
		for(int j =0;j<5;j++){
			if(str1[i] == a[j]){
				cout << a[j];
				temp=1;
				break;
			}
		}
	}
	if(temp==0){
		cout << 'n';
	}
	return 0;
}

