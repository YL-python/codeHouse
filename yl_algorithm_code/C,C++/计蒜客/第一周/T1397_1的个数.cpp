#include <iostream>
using namespace std;

int geshu(int x){
	int ans = 0;
	while(x){
		if(x % 2){
			ans ++;
		}
		x /= 2;
	}
	return ans;
}

int main(){
	int n,m;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> m;
		cout << geshu(m) << endl;
	} 
	return 0;
} 
