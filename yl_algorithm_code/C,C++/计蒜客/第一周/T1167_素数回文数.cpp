#include <iostream>
using namespace std;
int a[1005];

bool huiwen(int x){
	int a=x, b=0;
	while(a){
		b = b*10 + a%10;
		a/=10;
	}
	return b == x;
}

void shushu(){
	for(int i=2;i<1005;i++){
		for(int j=i+i;j<1005;j+=i){
			a[j] = 1;
		}
	}
}

int main(){
	int n,ans = 0;
	shushu();
	cin >> n;
	for(int i=11; i<=n; i++){
		if(a[i] == 0 && huiwen(i)){
			ans ++;
		}
	}
	cout << ans;
	return 0;
}
