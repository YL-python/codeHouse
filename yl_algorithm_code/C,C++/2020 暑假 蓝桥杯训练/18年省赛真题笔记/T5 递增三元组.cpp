#include <iostream>
#include <algorithm>
using namespace std;

int n,p,q;
int a[100005],b[100005],c[100005];

int main() {
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	for(int i=0; i<n; i++) {
		cin >> b[i];
	}
	for(int i=0; i<n; i++) {
		cin >> c[i];
	}
	sort(a,a+n);
	sort(b,b+n);
	sort(c,c+n);
	long long ans = 0;
	for(int i=0; i<n; i++) {
		while(p<n && a[p] < b[i]) p++;
		while(q<n && c[q] <= b[i]) q++;
		ans += (long long ) p*(n-q);
	}
	cout << ans;
	return 0;
}

/*
3
1 1 1
2 2 2
3 3 3

27
*/
