#include <iostream>
#include <string>
#include <queue>

using namespace std;

queue<int> q;
int n,m,ans,temp;
int a[1005];
int vis[1005];  // �ڴ�������û��

int main() {
	cin >> m >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];

		if( !vis[a[i]] ) { // �ڴ�����û��
			ans++;  // ȥ����һ��
			vis[a[i]] = 1;
			q.push(a[i]);
			if(q.size() > m) { // �ڴ�����
				vis[q.front()] = 0;
				q.pop();
			}
		}
		// �ڴ�������ɶ�¶���Ҫ����ֱ����һ�� 
	}
	cout << ans;
	return 0;
}




























