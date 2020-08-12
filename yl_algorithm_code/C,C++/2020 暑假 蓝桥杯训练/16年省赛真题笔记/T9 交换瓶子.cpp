#include<iostream>
using namespace std;
int n,a[10005],ans;

int pos(int x) {
	for(int i=1; i<=n; i++) {
		if(a[i] == x)
			return i;
	}
}
void swap(int i,int j) {
	int t = a[i];
	a[i] = a[j];
	a[j] = t;
}

int main() {
	cin >> n;
	for(int i=1; i<=n; i++) {
		cin >> a[i];
	}
	for(int i=1; i<=n; i++) {
		if(a[i] == i) continue;
		else {
			swap(pos(i),i);
			ans++;
		}
	}
	cout << ans;
	return 0;
}
