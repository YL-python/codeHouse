/*
二分必定正确的写法

r-l >5 的区间二分
剩下5个区间自己枚举
*/
#include <cstdio>

int f(int n) {
	if(n>100)
		return 1;
	return 0;
}// 第一个是1的下标是101  用二分找出

void search() {
	int l=1,r=1024,mid;
	while(r-l>5) {
		printf("[%d, %d]\n",l,r);
		mid = (l+r)/2;
		if(f(mid) == 0)
			l=mid+1;
		else
			r=mid;
	}
	for(; f(l)==0; l++);
	printf("%d\n",l);
}

int main() {
	search();
	return 0;
}
