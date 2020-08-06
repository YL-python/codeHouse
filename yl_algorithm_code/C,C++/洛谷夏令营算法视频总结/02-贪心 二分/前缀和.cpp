/*
前缀和
a数组 给定多个 l,r区间 求 l到r的和

sum[i]表示a数组前 i项和  求a数组的 l-r 区间和 就是求 sum[r+1] - sum[l]
*/

#include <cstdio>

int get_lr_sum(int l,int r) {
	return sum[r+1] - sum[l];
}

int main() {

	for(int i=0; i<n; i++) {
		scanf("%d",&a[i]);
		sum[i] += a[i];
	}

	return 0;
}
