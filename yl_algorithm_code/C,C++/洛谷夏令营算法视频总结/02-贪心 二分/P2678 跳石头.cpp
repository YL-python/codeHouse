/*
移动至少 m 块石头 表示不一定要移动 m 块石头 小于也是可以的，所以难度不在m这里

题目要求的是最大的 最短跳跃值，也就说在某一个临界点的时候，左边都可以，右边都不可以
是一个 0  1 的单调序列，就可以用二分来找到这个临界值

跳跃值为 x 的时候计算出移动石头的个数
大于 m 就是 0  小于m就是1
*/
#include <cstdio>

int l,n,m,a[50005];

// 跳跃值为 x 时我们要移动的石头数量
int f(int x) {
	int now=0,s=0;
	for(int i=1; i<=n; i++) {  // 起点跳到第一块石头上
		if(a[i] - a[now] < x) {
			s++;  // 移动石头 +1
		} else {
			now = i; // 跳到下一个石头上
		}
	}
	return s;
}

int main() {
	scanf("%d%d%d",&l,&n,&m);
	a[0] = 0;  // 起点
	for(int i=1; i<=n; i++)  // 第一块石头开始输入
		scanf("%d",&a[i]);

	// 二分查找跳跃值 mid
	int left=1,right=l,mid,ans;
	while(left <= right) {
		mid = (left + right) / 2;
//		printf("%d %d %d %d\n",s,left,right,mid);
		if(f(mid) <= m) {
			ans = mid;
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}
	printf("%d",ans);
	return 0;
}

/*
[00001111111]  用二分来查找第一个1出现的位置
题目难在怎么把关系转成 0  1 数组
假设每一次跳 (0+L)/2 个距离  看看 移动的石头是否满足
找到满足关系的时候  跳跃的最大值就是我们需要的答案了
*/
