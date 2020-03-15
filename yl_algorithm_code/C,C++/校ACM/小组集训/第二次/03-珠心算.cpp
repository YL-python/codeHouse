#include <iostream>
#include <algorithm>
using namespace std;

// 数据范围100 没啥好说的  暴力
int n,cnt;
int a[105];
int vis[10005];  // 记录那些数出现过 

int main() {
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];
		vis[a[i]] = 1; // 这个数出现过 
	}
	int ans = 0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<i; j++) {
			// vis 数组越界问题 
			if(a[i] + a[j] <= 10000 &&  vis[a[i] + a[j]]) { // 这个数出现过
				ans ++;
				// 用过的数就不能在计算 不然答案就多了。 
				vis[a[i] + a[j]] = 0;
			}
		}
	}
	cout << ans;
	return 0;
}
