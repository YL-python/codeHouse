#include <cstdio>

int a,b;

bool ss_book[10000001];

void make_ss() {
	ss_book[0]=ss_book[1] = false;
	for(int i=2; i<=9999999; i++) {
		for(int j=i*2; j<=9999999; j+=i) {
			ss_book[j] = true;
		}
	}
}

bool huiwen(int x) {
	int temp = x;
	int cnt=0;
	while(temp) {
		cnt = cnt*10 + temp%10;
		temp /= 10;
	}
	if(cnt == x) {
		return true;
	} else {
		return false;
	}
}

int main() {

	scanf("%d%d",&a,&b);
	//b<=10000000这个判断条件来自：除了11以外，一个数的位数是偶数的话，不可能为回文数素数。
	// 如果一个回文素数的位数是偶数，则它的奇数位上的数字和与偶数位上的数字和必然相等；
	// 根据数的整除性理论，容易判断这样的数肯定能被11整除，所以它就不可能是素数。
	if (b>=10000000)
		b=9999999;
	for(int i=a; i<=b; i++) {
		if(! ss_book[i]) {
			if(huiwen(i)) {
				printf("%d\n",i);
			}
		}
	}
	return 0;
}
