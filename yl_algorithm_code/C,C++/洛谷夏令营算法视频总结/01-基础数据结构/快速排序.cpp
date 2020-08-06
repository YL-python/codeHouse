#include <cstdio>

int a[1000005],n;

void qsort(int l,int r) {
	int i=l, j=r, mid=a[(l+r)/2];
	while(i<=j) {  // 允许他们指向同一个数
		while(a[i]<mid) {
			// a[i] 比 mid 小的时候就会一直加  直到这个值大于等于 mid 就会停下
			i++;
		}
		while(a[j]>mid) {
			// a[j] 大于 mid 的时候就会一直减  直到这个值小于等于  mid 就会停下
			j--;
		}
		// 这个时候 i 是大于等于 mid 的下标  j 是小于等于 mid 的下标
		if(i<=j) {
			int t=a[i];
			a[i] = a[j];
			a[j] = t;
			// 这里强制的 ++ -- 就能避免掉他们指向同一个数不动的情况
			i++;
			j--;
		}
	}
	// 这个时候 数组分两边 [] mid []  左边全是小于mid等于 的 右边全是大于等于mid 的
	// i 就指向第一个等于 mid 的下标+1  j 就是指向左边数组小于 mid 的下标-1

	if(l<j) qsort(l,j);//递归搜索左半部分
	if(i<r) qsort(i,r);//递归搜索右半部分
}

int main() {
	scanf("%d",&n);
	for(int i=1; i<=n; i++) {
		scanf("%d",&a[i]);
	}
	qsort(1,n);
	for(int i=1; i<=n; i++) {
		printf("%d ",a[i]);
	}
	return 0;
}
