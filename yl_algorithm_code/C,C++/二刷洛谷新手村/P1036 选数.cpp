#include <iostream>
using namespace std;

int a[25],n,k,ans=0;

int ss(int x) {
	for(int i=2; i*i<=x; i++) {
		if(x % i == 0) {
			return 0;
		}
	}
	return 1;
}

// 第 cen 上的数  cet表示选还是不选  sum表示当前的和
void dfs(int cen,int cnt, int sum) {
	if(cen == n) {  // 在最后 n 层了
		if(cnt == k) {  // 选了数量为 k 个的时候
			if(ss(sum)) {
				ans++;
			}
		}
		return ;
	}
	dfs(cen+1,cnt,sum);  // 进入下一层 并且当前层上的数不选
	dfs(cen+1,cnt+1,sum+a[cen]);  // 进入下一层 并且当前层上的数选
}

int main() {
	cin >> n >> k;
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	dfs(0,0,0);
	cout << ans;
	return 0;
}
