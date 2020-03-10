#include <iostream>
#include<cmath>
using namespace std;

int a[1000005];
long long b[10000];
int b_index=0;

// 素数返回 true 
bool ss(long long x){
	int cnt = sqrt(x);
	for(int i=2;i<=cnt;i++){
		if(x%i == 0){
			return false;
		}
	}
	return true;
}

int main() {
	long long n;
	cin >> n;
	int cnt = sqrt(n);
	for(int i=1; i<=cnt; i++) {
		if(n%i == 0) {
			long long temp = n/i;
			// temp 和 i都是 n 的因子
			// b 数组用来装 n 的因子，装之前判断有没有出现过，出现过就不装 
			bool flag = false;
			for(int j = 0; j<b_index; j++) {
				if(b[j] == i) {
					flag = true;
				}
			}
			if(!flag) {
				b[b_index++] = i;
			}
			flag = false;
			for(int j = 0; j<b_index; j++) {
				if(b[j] == temp) {
					flag = true;
				}
			}
			if(!flag) {
				b[b_index++] = temp;
			}
		}
	}
	long long ans = 1;
	for(int j = 0; j<b_index; j++) {
		if(ss(b[j])){
			ans *= b[j];
		}
	}
	cout << ans;
}
/*
蓝桥杯的样例数据：
533 533
6021 669
1911 273
770518 770518
887244 443622
79561585 79561585
80189196 40094598
81095240 20273810
1822020238 1822020238
18374001125 734960045
*/

