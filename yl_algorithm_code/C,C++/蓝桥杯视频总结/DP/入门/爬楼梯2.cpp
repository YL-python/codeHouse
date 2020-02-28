#include <iostream>
using namespace std;
const int mod = 100007;
int dp[1010];
// 可以跳过任意奇数楼梯 
int main() {
	int n;
	cin >> n;
	dp[0] = 1;
	for(int i=1;i<=n;i++){
		dp[i] = 0;
		// -1  -3  -5  -7
		for(int j=i-1;j>=0;j-=2){
			dp[i] += dp[j];
			dp[i] %= mod;
		} 
	}
	cout << dp[n] << endl;
	return 0;
}

