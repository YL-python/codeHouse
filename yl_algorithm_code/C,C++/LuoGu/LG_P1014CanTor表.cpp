#include <iostream>
#include <string>

using namespace std;

int n; 

int main(){
	cin >> n;
	int i=0,j=0;
	while(n>j){
		i+=1;
		j+=i;
	}
	
	if(i % 2 == 0){
		cout << i+n-j << "/" << j-n+1;
	}else{
		cout << j-n+1 << "/" << i+n-j;
	}
	return 0;
}




























