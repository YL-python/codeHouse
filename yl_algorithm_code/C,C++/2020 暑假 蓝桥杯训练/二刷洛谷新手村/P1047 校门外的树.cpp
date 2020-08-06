#include <iostream>
using namespace std;

int l,m,u,v,ans;
int vis[10005];

int main() {
	cin >> l >> m;
	for(int i=0; i<m; i++) {
		cin >> u >> v;
		for(int j=u; j<=v; j++) {
			vis[j] = 1;
		}
	}
	for(int i=0; i<=l; i++) {
		vis[i] == 0 ? ans++ : 1;
	}
	cout << ans;
	return 0;
}
