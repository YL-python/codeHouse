#include<cstdio>
#include<algorithm>
using namespace std;
int a[] = {1,2,3,4,5,6,7,8,9},ans;
bool check() {
	int x = a[3] * 100 + a[4] * 10 + a[5];
	int y = a[6] * 100 + a[7] * 10 + a[8];
	if((a[1] * y + a[2] * x) % (y * a[2]) == 0 && a[0] + (a[1] * y + a[2] * x) / (y * a[2]) == 10)return true;
	return false;
}
// 递归回溯生成全排列  适用于无重复元素的情况
void f(int k) {
	if(k == 9) {
		if(check()) ans++;
	}
	// 从第k位开始 把数组的每一项都放在 k位上尝试
	for(int i=k; i<9; i++) {
		{ int t=a[i]; a[i]=a[k]; a[k]=t; }
		f(k+1);  // 递归
		{ int t=a[i]; a[i]=a[k]; a[k]=t; }  // 回溯
	}
}
int main() {
//	f(0);
	do{
		if(check()) ans++;
	}while(next_permutation(a,a+9));
	printf("%d\n",ans);
	return 0;
}
