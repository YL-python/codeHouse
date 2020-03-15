#include <iostream>
#include <algorithm>
using namespace std;

// 分段函数 ，最后向上取整

int before(double d, double t) {
	double ans = 0.0;
	ans = (t/5) * 2;
	ans += 1.0;
	if(d <= 3) {
		ans += 10;
	} else if(d<=10) {
		ans += 10;
		ans += (d-3) * 2;
	} else {
		ans += 10;
		ans += 14;
		ans += (d-10) * 3;
	}
	return int (ans + 0.5);
}

int after(double d, double t) {
	double ans = 0.0;
	ans = t/4;
	ans *= 2.5;
	if(d <= 3) {
		ans += 11;
	} else if(d<=10) {
		ans += 11;
		ans += (d-3) * 2.5;
	} else {
		ans += 11;
		ans += 7*2.5;
		ans += (d-10) * 3.75;
	}
	return int (ans + 0.5);
}

int main() {

	int T;
	double d,t;
	cin >> T;
	for(int i=0; i<T; i++) {
		cin >> d>> t;
		cout << after(d,t) - before(d,t)<<endl;
	}
	return  0;
}
