#include <iostream>
using namespace std;
const int mod = 100007;
int dp[1010];

int main() {
	int n;
	cin >> n;
	dp[1] = dp[0] = 1;
	for(int i=2;i<=n;i++){
		dp[i] = (dp[i-1] % mod + dp[i-2] % mod) % mod;
	}
	cout << dp[n] << endl;
	return 0;
}

