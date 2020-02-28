#include <iostream>
#include <string>
using namespace std;

int jiechen(int x){
	int sum=0;
	for(int i=1;i<=x;i++){
		int m=1;
		for(int j=1;j<=i;j++){
			m*=j;
		}
		sum+=m;
	}
	return sum;
}

int main(){
	int T,n[15],ans[15];
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> n[i];
		cout << jiechen(n[i])<<endl;
	}
	
	return 0;
}

