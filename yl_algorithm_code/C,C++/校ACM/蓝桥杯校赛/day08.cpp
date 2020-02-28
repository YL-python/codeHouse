#include <iostream>
#include <string>
using namespace std;

int main(){
	int n,a[100005];
	long long ans=0;
	cin >> n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	if(n == 1){
		cout << 0;
	}else{
		for(int i=1;i<n;i++){
			for(int j=i-1;j>=0;j--){
				if(a[j]>a[i]){
					ans += i-j;
					break;
				}
			}
		}
		cout << ans;
	}
	
	return 0;
}

