#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int n,ans = 2,cnt = 1,mod = 50000;
	int i = 3;
	bool flag;

	cin >> n;

	while(n > cnt) {
		flag = true;
		for(int j = 2; j<sqrt(i) + 1; j++) {
			if(i % j == 0) {
				flag = false;
				break;
			}
		}
		if(flag) {
			cnt++;
			ans %= mod;
			ans *= i;
			ans %= mod; 
		}
		i ++;
	}
	cout << ans;
	return  0;
}
