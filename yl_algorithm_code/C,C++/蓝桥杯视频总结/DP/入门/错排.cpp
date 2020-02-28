#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1e3 + 9;
int f[N];
int main() {
	int n;
	cin >> n;
	f[1] = 0;
	f[2] = 1;
	for(int i=3; i<=n; i++) {
		f[i] = (f[i-1] + f[i-2]) * (i - 1);
	}
	cout << f[n] << endl;
	return 0;
}
/*
	错排公式：
	fn = (n - 1) * ( fn-1 + fn-2)
	
	n 个错排 方案是 F(n)，递推考虑
	n-1 个错牌之后,拿第n封信 去交换  就是F(n-1) * n-1
	还有情况就是 n-1里面有一个是对的 n-2进行错排，然后 第n封信去个这个对的交换
	就是 F(n-2) * n-1
	和就是  fn = (n - 1) * ( fn-1 + fn-2)
	
	考虑边界， F1 = 0，F2 = 1 
*/
