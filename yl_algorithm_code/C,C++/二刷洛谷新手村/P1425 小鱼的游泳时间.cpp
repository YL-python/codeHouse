#include <cstdio>

int h1,h2,m1,m2,sum;

int getmin(int h,int m) {
	return h*60+m;
}

int main() {

	scanf("%d%d%d%d",&h1,&m1,&h2,&m2);

	int ans = getmin(h2,m2) - getmin(h1,m1);

	printf("%d %d",ans/60,ans%60);

	return 0;
}
