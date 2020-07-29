#include <iostream>
using namespace std;

int vis[10] = {6,2,5,5,4,5,6,3,7,6};

int fun(int x) {
	int y=0;
	if(x == 0) {
		y = vis[0];
	} else {
		while(x) {
			y += vis[x%10];
			x/=10;
		}
	}
	return y;
}

int main() {
	int n,ans=0,temp;
	cin >> n;
	n-=4;
	for(int i=0; i<1000; i++) {
		for(int j=0; j<1000; j++) {
			if(fun(i) + fun(j) + fun(i+j) == n) {
				ans++;
			}
		}
	}
	cout << ans;
	return 0;
}
