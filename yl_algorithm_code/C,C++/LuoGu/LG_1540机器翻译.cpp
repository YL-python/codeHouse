#include <iostream>
#include <string>
#include <queue>

using namespace std;

queue<int> q;
int n,m,ans,temp;
int a[1005];
int vis[1005];  // 内存里面有没有

int main() {
	cin >> m >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];

		if( !vis[a[i]] ) { // 内存里面没有
			ans++;  // 去外存查一次
			vis[a[i]] = 1;
			q.push(a[i]);
			if(q.size() > m) { // 内存满了
				vis[q.front()] = 0;
				q.pop();
			}
		}
		// 内存里面有啥事都不要做，直接下一个 
	}
	cout << ans;
	return 0;
}




























