#include <cstdio>
#include <queue>
using namespace std;

int a[1005]= {0},n,m,temp,ans;
queue <int> q;

int main() {

	scanf("%d%d",&n,&m);
	while(m--) {
		scanf("%d",&temp);
		// 检查内存
		if(a[temp] == 0) {  // 没有
			ans++;  // 查询次数 +1;
			a[temp] = 1;
			q.push(temp);
			if(n == 0) { // 内存容量
				int cnt = q.front();
				q.pop();
				a[cnt] = 0;
			} else {
				n--;
			}
		}
	}

	printf("%d",ans);

	return 0;
}
