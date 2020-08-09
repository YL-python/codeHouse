#include <iostream>
#include <cmath>
using namespace std;

typedef long long LL;
LL x,y,d,n;

LL sum(LL a0,LL n,LL d) {
	return (a0*2 + d*(n-1)) * n / 2;
}

int main() {
	cin >> x >> y;
	if(y>0 && abs(x) <= y) {  // 落在上方
		n = y;
		d = y-x + 2*y;
	} else if(x > 0 && abs(y) <= x) {  // 落在右方
		n = x;
		d = x+y;
	} else if(y <= 0 && x >= y-1 && x<=-y) {  // 落在右方
		n=-y;
		d = -(-y-x);
	} else if(x<0&&y>=x+1 && y<=-x) {  // 落在右方
		n = -x-1;
		d = -(y-x-1-2*x-1);
	}
	cout << sum(1, 2*n, 1) * 2 - d <<endl;
	return 0;
}
