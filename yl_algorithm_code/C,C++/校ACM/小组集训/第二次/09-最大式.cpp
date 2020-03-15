#include <iostream>
#include <algorithm>
using namespace std;

long long int dp[20][20];
int sum[16];

// 深搜暴力，最坏情况是8的阶层种情况，也不会爆
// 但是把  能深搜的最后都能转成dp 
 
int main() {
    int n, k;
    cin >> n >> k;
    for(int i = 1; i <= n; i++) {
        int temp;
        cin >> temp;
        sum[i] =  sum[i-1] + temp;
    }
    for(int i = 1; i <= n; i++) {
        dp[i][0] = sum[i];
    }
    for(int i = 2; i <= n; i++) {
        for(int j = 1; j <= i-1 && j <= k; j++) {
            for(int l = 2; l <= n; l++) {
                dp[i][j] = max(dp[i][j], dp[l-1][j-1] * (sum[i] - sum[l-1]));
            }
        }
    }
    cout << dp[n][k];
    return 0;
}
