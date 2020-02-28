#include <iostream>
using namespace std;

int main(){
	int a[10] = {6,2,5,5,4,5,6,3,7,6};
	int b[2001] = {6}; // b{0} = 6 
	int n,ans = 0;
	cin >> n;
	// 从 1 开始， 0进不去 
	for(int i=1;i<2001;i++){
		int j=i;
		while(j>=1){
			b[i] += a[j%10];
			j/=10;
		}
	}
	for(int i=0;i<1000;i++){
		for(int j=0;j<1000;j++){
			if(b[i] + b[j] + b[i+j] +4 == n){
				ans++;
			}
		}
	}
	cout << ans;
	return 0;
}
