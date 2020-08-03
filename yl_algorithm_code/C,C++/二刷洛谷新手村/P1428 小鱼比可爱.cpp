#include <cstdio>

int n,a[35];

int main() {

	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&a[i]);
	}

	int cnt;
	for(int i=0; i<n; i++) {
		cnt = 0;
		for(int j=0; j<i; j++) {
			if(a[i] > a[j]) {
				cnt++;
			}
		}
		printf("%d ",cnt);
	}

	return 0;
}
