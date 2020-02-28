#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 100010;
int dp[maxn],a[maxn];

// 落在弹簧板的任意位置 求最多多少次弹出 

int main() {
	int n;
	cin >> n;
	memset(dp, 0, sizeof(dp));
	for(int i=1;i<=n;i++){
		cin >> a[i];
	}
	// 还有多少步弹出弹簧板  反着考虑 
	int ans = 0;
	for(int i=n; i>=1; --i){
		// 当前一步 还要弹多少下才能出去
		// 他能弹道的位置 上的步数加一 
		dp[i] = dp[i + a[i]] + 1;
		ans = max(ans, dp[i]);
	}
	cout << ans << endl;
	return 0;
}

