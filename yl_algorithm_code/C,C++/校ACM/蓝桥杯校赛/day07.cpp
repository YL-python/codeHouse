#include <iostream>
#include <string>
using namespace std;

int main(){
	int count=0,n;
	cin>>n;
	for(int i =1;i<=n;i++){
		int j=i,k=0;
		while(j!=0){
			k = j%10;
			j=j/10;
			if(k==2){
				count++;
				break;
			}
		}
	}
	cout << n-count;
	return 0;
}

