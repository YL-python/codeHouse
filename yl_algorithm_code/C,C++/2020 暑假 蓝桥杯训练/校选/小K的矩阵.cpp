#include<stdio.h>
#include<math.h>

long long ans,n;
long long MOD = 1000000007;
long long a[100005];

void count2(int x) {
	int n = x/2;
	int num = 0,temp=0;
	for(int i=n; i>=1; i--) {
		num += (temp * i * 4 + 4 * i);
		num %= MOD;
		temp += 2;
	}
	num %= MOD;
	ans = num;
}

void count1(int x) {
	int n = x / 2 + 1;
	int num = 0,temp=0;
	for(int i=n; i>=1; i--) {
		if(temp == 0) {
			num += i;
			num %= MOD;
		} else {
			num += (temp * i * 4 + 4 * i);
			num %= MOD;
		}

		if(temp == 0) {
			temp += 1;
		} else {
			temp += 2;
		}
	}
	num %= MOD;
	ans = num;
}

int main() {
	int t;
	scanf("%d",&t);

	for(int i=0; i<=100000000; i++) {

	}



	for(int i=0; i<t; i++) {
		scanf("%d",&a[i]);
	}
	return 0;
}

