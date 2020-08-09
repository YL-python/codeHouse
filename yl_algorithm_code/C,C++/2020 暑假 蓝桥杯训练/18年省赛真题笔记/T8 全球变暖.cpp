#include <cstdio>
#include <queue>
using namespace std;

char map[1005][1005];
int vis[1005][1005],n,ans;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

struct Point {
	int x,y;
};

void bfs(int i,int j) {
	vis[i][j] = 1;  // 标记为访问过了
	queue<Point> q;  // 一个队列就是一块 
	q.push({i,j});
	int cnt1=0,cnt2=0; // 记录当前块 # 的数量 和 淹没的数量
	while(! q.empty()) {
		Point first = q.front();
		q.pop();
		cnt1++;  // # 号数量加一 
		bool swed = false;  // 记录这个块的 # 号周围是不是有 .
		for(int i=0; i<n; i++) {
			int x = first.x + dx[i];
			int y = first.y + dy[i];
			if(0<=x && x<n && 0<=y && y<n && map[x][y] == '.') {
				swed = true; // # 周围有 .
			}
			if(0<=x && x<n && 0<=y && y<n && map[x][y] == '#' && vis[x][y] == 0) {
				q.push({x,y});  // 吧周围的 # 号加如队列中并且标记访问
				vis[x][y] = 1;
			}
		}
		if(swed) cnt2++; // 淹没的数量加一
	}
	// #号和淹没的数量相等的时候这块岛屿就没了 
	if(cnt1 == cnt2) ans++;
}


int main() {
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			scanf("%c",&map[i][j]);
		}
	}
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			if(map[i][j] == '#' && vis[i][j] == 0) {
				bfs(i,j);
			}
		}
	}
	printf("%d",ans);
	return 0;
}
