#include <iostream>
using namespace std;

// 解法 2 记忆递归  时间复杂度 N的平方

int n,ans = 1;
int vis[1005];

int fun(int x) {
	if(x == 1) {
		return 1;
	}
	if(vis[x]) return vis[x];
	int res = 0;
	for(int i=1; i<=x/2; i++) {
		res += fun(i);
	}
	vis[x] = res + 1;  // 加上自身
	return vis[x];
}

int main() { 
	cin >> n;
	cout << fun(n);
	return 0;
}
