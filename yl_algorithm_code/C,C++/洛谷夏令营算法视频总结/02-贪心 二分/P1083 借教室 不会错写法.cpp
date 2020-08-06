// 直接暴力时间 n*m  超时
// 二分就是 m* log2 n
// 1-x 天都满足  x-n天都不满足  就是 1  0 单调序列啊

#include<cstdio>
#include<cstring>

int m,n,jiaoshi[1000005];
int dindan[1000005][3],p[1000005],a[1000005];

// 求 1-x的区间的订单能不能满足条件
int f(int x) {
	// 差分数组求区间和
	memset(p,0,sizeof(p));
	for(int i=1; i<=x; i++) {
		p[dindan[i][1]] += dindan[i][0];
		p[dindan[i][2] + 1] -= dindan[i][0];
	}
	for(int i=1; i<=n; i++) {
		a[i] = a[i-1]+p[i];
		if(a[i] > jiaoshi[i])
			return 0;
	}
	return 1;
}

int main() {
	scanf("%d%d",&n,&m);

	for(int i=1; i<=n; i++) {
		scanf("%d",&jiaoshi[i]);
	}
	for(int i=1; i<=m; i++) {
		scanf("%d%d%d",&dindan[i][0],&dindan[i][1],&dindan[i][2]);
	}

	if(f(m)) {
		printf("0");
		return 0;
	}

	int left=1,right=m,mid;
	while((right -left) > 5) {
		mid = (left+right) / 2;

		if(f(mid)) {
			left = mid+1;
		} else {
			right = mid-1;
		}
	}

	for(; f(left); left++);

	printf("-1\n");
	printf("%d",left);
	return 0;
}
