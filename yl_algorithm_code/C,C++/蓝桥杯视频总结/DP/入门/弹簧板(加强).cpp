#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 100010;
int dp[maxn],a[maxn];

// ���ڵ��ɰ������λ�� �������ٴε��� 

int main() {
	int n;
	cin >> n;
	memset(dp, 0, sizeof(dp));
	for(int i=1;i<=n;i++){
		cin >> a[i];
	}
	// ���ж��ٲ��������ɰ�  ���ſ��� 
	int ans = 0;
	for(int i=n; i>=1; --i){
		// ��ǰһ�� ��Ҫ�������²��ܳ�ȥ
		// ���ܵ�����λ�� �ϵĲ�����һ 
		dp[i] = dp[i + a[i]] + 1;
		ans = max(ans, dp[i]);
	}
	cout << ans << endl;
	return 0;
}

