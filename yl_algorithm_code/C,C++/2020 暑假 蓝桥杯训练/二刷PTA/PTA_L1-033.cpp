#include<stdio.h>

// 给一个数，返回这个数有几个数是互不相同的
int fun(int x) {
	int ans=0,sum[10]= {0};
	int temp = 0;
	if(x < 1000) {
		sum[0] = 1;
	}
	while(x) {
		temp = x % 10;
		x /= 10;
		sum[temp] = 1;
	}
	for(int i=0; i<10; i++) {
		ans += sum[i];
	}
	return ans;
}

int main() {

	int x,y,n;
	scanf("%d %d",&y,&n);
	x = y;

	while(fun(x) != n) {
		x+=1;
	}

	printf("%d %04d", x-y,x);
	return 0;
}

