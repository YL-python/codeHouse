#include <iostream>
using namespace std;
int n,m;
long long ans;
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> m;
		if(m % 2 == 0){
			ans += m;
		}
	}
	cout << ans;
	return 0;
} 
