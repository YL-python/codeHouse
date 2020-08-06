#include <cstdio>

int n,a[1000005],ans=1,cnt=1;

int main() {
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&a[i]);
	}

	for(int i=1; i<n; i++) {
		if(a[i] > a[i-1]) {
			cnt++;
		} else {
			if(cnt > ans) {
				ans = cnt;
			}
			cnt=1;
		}
	}
	if(cnt > ans) {
		ans = cnt;
	}
	printf("%d",ans);

	return 0;
}
