#include <iostream>
#include <algorithm>
using namespace std;

int a[1005];

int bignum(int l,int r,int k) {
	int b[1005];
	int cnt = 0;
	for(int i=l-1; i<r; i++) {
		b[cnt++] = a[i];
	}
	sort(b,b+cnt);
	return b[cnt - k];
}

int main() {
	int n,t;
	int l,r,k;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	cin >> t;
	for(int i=0; i<t; i++) {
		cin >> l >> r >> k;
		cout << bignum(l,r,k) << endl;
	}
	return  0;
}
