#include <iostream>
using namespace std;

int main() {
	int n,k;
	int h[100000],w[100000];
	cin >> n >> k;
	for(int i=0; i<n; i++) {
		cin >> h[i] >> w[i];
	}
	int r = 100001;
	int l = 1;
	int ans;
	while(l <= r) {
		int mid = (l+r) / 2;
		int cnt = 0;
		for(int i=0; i<n; i++) {
			cnt += (h[i] / mid) * (w[i] / mid)
		}
		if(cnt > mid) {
			l = mid + 1;
			ans = mid;
		} else {
			r = mid - 1;
		}
	}
	printf("%d",ans);
	return 0;
}
