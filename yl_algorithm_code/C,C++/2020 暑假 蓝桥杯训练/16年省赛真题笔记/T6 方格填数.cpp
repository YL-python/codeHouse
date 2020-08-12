#include <cstdio>
#include <cmath>
int a[] = {0,1,2,3,4,5,6,7,8,9},ans;

bool check() {
	if(
	    abs(a[0] - a[1]) == 1||
	    abs(a[0] - a[3]) == 1||
	    abs(a[0] - a[4]) == 1||
	    abs(a[0] - a[5]) == 1||

	    abs(a[1] - a[2]) == 1||
	    abs(a[1] - a[4]) == 1||
	    abs(a[1] - a[5]) == 1||
	    abs(a[1] - a[6]) == 1||

	    abs(a[2] - a[5]) == 1||
	    abs(a[2] - a[6]) == 1||

	    abs(a[3] - a[4]) == 1||
	    abs(a[3] - a[7]) == 1||
	    abs(a[3] - a[8]) == 1||

	    abs(a[4] - a[5]) == 1||
	    abs(a[4] - a[7]) == 1||
	    abs(a[4] - a[9]) == 1||
	    abs(a[4] - a[8]) == 1||

	    abs(a[5] - a[6]) == 1||
	    abs(a[5] - a[9]) == 1||
	    abs(a[5] - a[8]) == 1||

	    abs(a[6] - a[9]) == 1||
	    abs(a[7] - a[8]) == 1||
	    abs(a[8] - a[9]) == 1	)
		return false;
	return true;
}

void f(int k) {
	if(k == 10) {
		if(check())
			ans++;
	}
	for(int i=k; i<10; i++) {
		{ int t=a[i]; a[i]=a[k]; a[k]=t; }
		f(k+1);
		{ int t=a[i]; a[i]=a[k]; a[k]=t; }
	}
}

int main() {
	f(0);
	printf("%d\n",ans);
	return 0;
}
/*
{ int t=a[i]; a[i]=a[k]; a[k]=t; }
*/
