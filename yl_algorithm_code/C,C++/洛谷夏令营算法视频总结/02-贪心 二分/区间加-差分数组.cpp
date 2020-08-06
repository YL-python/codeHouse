/*
a数组 在 l,r范围内每一次加上k
多次执行   要求时间复杂度是 On

知道每一个元素比前面元素多几就能推出这个数组

l 到 r 的区间加k就是
a[l] 开始比前面一个元素多 k , a[r+1] 开始比前面每个元素少 k

用一个数组表示 每一个元素和前一个元素的差
p[i] = a[i] - a[i-1]

l 到 r 的区间加k就变成了
p[l]+=k
p[r+1]-=k
*/
#include <cstdio>

int a[100],p[100];

void add(int l,int r,int k) {
	p[l]+=k;
	p[r+1]-=k;
}

void get_a() {
	for(int i=1; i<=n; i++) {
		a[i] = a[i-1]+p[i];
	}
}

int main() {

	return 0;
}
