#include <cstdio>
int n,a[105],g;
bool f[10000];  // 100*100-100-100
int gcd(int a,int b) {
	return b?gcd(b,a%b):a;
}
int main() {
	f[0] = true;
	scanf("%d",&n);
	for(int i=1; i<=n; i++) {
		scanf("%d",&a[i]);
		if(i == 1) g = a[i];
		else g = gcd(a[i],g);
		for(int j=0; j<10000; j++) {
			if(f[j]) f[j + a[i]] = true;
		}
	}
	if(g != 1) {
		printf("INF\n");
		return 0;
	}
	// 统计个数
	int ans =0;
	for(int i=0; i<10000; i++) {
		if(! f[i])ans++;
	}
	printf("%d\n",ans);
	return 0;
}
