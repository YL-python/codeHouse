#include <cstdio>
typedef long long LL;
const int N = 5000;

bool isPrime(LL x) {
	bool ans = true;
	for(LL i=2; i*i<x; i++) {
		if( x % i == 0) {
			ans = false;
		}
	}
	return ans;
}

LL fun(LL a[], int n) {
	for(int i=0; i<n; i++) {// ö����������
		for(int d=1; d<n; d++) {// ö�ٹ���
			LL first = a[i];
			int cnt=1;
			for(int j=1; j<=9; j++) { // ö��10��
				LL ax = first + d*j;
				if(isPrime(ax)) {
					cnt++;
				} else {
					break;
				}
			}
			if(cnt == 10) {
				return d;
			}
		}
	}
	return -1;
}

int main() {
	LL a[N];
	a[0] = 2;
	a[1] = 3;
	a[2] = 5;
	LL t = 6;
	LL index = 3;
	while(index < N) {
		if(isPrime(t)) {
			a[index ++] = t;
		}
		t++;
	}
	printf("%d \n",fun(a,N));
	return 0;
}
