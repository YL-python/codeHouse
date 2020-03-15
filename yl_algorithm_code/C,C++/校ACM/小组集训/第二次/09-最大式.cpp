#include <iostream>
#include <algorithm>
using namespace std;

long long int dp[20][20];
int sum[16];

// ���ѱ�����������8�Ľײ��������Ҳ���ᱬ
// ���ǰ�  �����ѵ������ת��dp 
 
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
