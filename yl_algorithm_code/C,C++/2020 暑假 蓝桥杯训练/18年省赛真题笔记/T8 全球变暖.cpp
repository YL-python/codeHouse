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
	vis[i][j] = 1;  // ���Ϊ���ʹ���
	queue<Point> q;  // һ�����о���һ�� 
	q.push({i,j});
	int cnt1=0,cnt2=0; // ��¼��ǰ�� # ������ �� ��û������
	while(! q.empty()) {
		Point first = q.front();
		q.pop();
		cnt1++;  // # ��������һ 
		bool swed = false;  // ��¼������ # ����Χ�ǲ����� .
		for(int i=0; i<n; i++) {
			int x = first.x + dx[i];
			int y = first.y + dy[i];
			if(0<=x && x<n && 0<=y && y<n && map[x][y] == '.') {
				swed = true; // # ��Χ�� .
			}
			if(0<=x && x<n && 0<=y && y<n && map[x][y] == '#' && vis[x][y] == 0) {
				q.push({x,y});  // ����Χ�� # �ż�������в��ұ�Ƿ���
				vis[x][y] = 1;
			}
		}
		if(swed) cnt2++; // ��û��������һ
	}
	// #�ź���û��������ȵ�ʱ����鵺���û�� 
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
