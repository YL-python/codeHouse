#include <iostream>
using namespace std;

// 数据范围是 10的五次方，直接两个for 暴力枚举不会超时
// 这题是标准的 dp 最大子序和

int main() {
	int n;
	int a[100005];
	int dp;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	dp = a[0];
	int ans = a[0];
	for(int i=1; i<n; i++) {
		dp = max(dp+a[i],a[i]);
		if(dp > ans){
			ans = dp;
		}
	}
	cout << ans;
	return 0;
}
