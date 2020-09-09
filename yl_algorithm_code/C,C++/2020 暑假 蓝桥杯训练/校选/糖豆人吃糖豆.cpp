#include<iostream>
#include<algorithm>
using namespace std;

int n,q,a[1000005],ans;

int main() {

	cin >> n >> q;
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	sort(a,a+n);

	for(int i=0; i<n; i++) {
		ans += a[i] * q;
		q+=1;
	}
	cout << ans << endl;
	return 0;
}

