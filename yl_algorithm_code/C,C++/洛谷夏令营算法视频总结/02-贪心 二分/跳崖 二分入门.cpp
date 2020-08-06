/*
跳崖
小止是一个睿智的mc玩家。mc里面是有掉落伤害的。
我们假设一次掉落要么不掉血，要么摔死人。
小止想知道，至少从多少层跳下来会摔死。
注意到mc里面死了可以重生，所以小止决定做实验:每次从某个高度跳下来。
要求给出一个方案，以最小的试验次数保证找出答案。
已知:从1024层跳下来biss.

每一次取中点 [1,512] [512,1024]

log2 1024 = 10
*/
#include <cstdio>

int f(int n) {
	if(n>100)
		return 1;
	return 0;
}// 第一个是1的下标是101  用二分找出

void search() {
	int l=100,r=102,mid;
	while(l != r) {
		printf("[%d, %d]\n",l,r);
		mid = (l+r)/2;
		if(f(mid) == 0)
			l=mid+1;
		else
			r=mid;
	}
	printf("%d\n",l);
}

int main() {
	search();
	return 0;
}
