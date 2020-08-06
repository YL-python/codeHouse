#include <cstdio>
#include <queue>
using namespace std;

queue<int> q;
int n,m;

int main() {
	scanf("%d%d",&n,&m);
	for(int i=1; i<=n; i++) {
		q.push(i);
	}
	int cnt=0,temp;
	while(!q.empty()) {
		cnt++;
		temp = q.front();
		q.pop();
		if(cnt == m) {
			printf("%d ",temp);
			cnt=0;
		} else {
			q.push(temp);
		}
	}
	return 0;
}
