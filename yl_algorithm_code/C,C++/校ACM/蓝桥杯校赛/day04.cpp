#include <iostream>
#include <string>
using namespace std;

int count=0,n=2019;

int main(){
	for(int i=1;i<=n;i++){
		int j=i,k=0;
		while(j){
			k = j % 10;
			j = j / 10;
			if(k == 9){
				count++;
				break;
			}
		}
	}
	cout << count;
	return 0;
}

