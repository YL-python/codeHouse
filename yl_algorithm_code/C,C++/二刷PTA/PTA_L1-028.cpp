#include<iostream>
#include<cmath>
using namespace std;

int issushu(int x) {
	if(x == 1) {
		return 0;
	}
	int sqrtx = sqrt(x);
	for(int i=2; i<=sqrtx; i++) {
		if (x % i == 0) {
			return 0;
		}
	}
	return 1;
}

int main() {
	int N,cnt;
	cin >> N;
	while(N --) {
		cin >> cnt;
		if(issushu(cnt)) {
			cout << "Yes" << endl;
		} else {
			cout << "No" << endl;
		}
	}
	return 0;
}
