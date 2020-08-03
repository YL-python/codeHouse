#include <cstdio>

double n,temp=2.0,cnt=0.0;
int ans=0;

int main() {

	scanf("%lf",&n);
	while(cnt < n) {
		cnt+=temp;
		temp*=0.98;
		ans++;
	}

	printf("%d",ans);

	return 0;
}
