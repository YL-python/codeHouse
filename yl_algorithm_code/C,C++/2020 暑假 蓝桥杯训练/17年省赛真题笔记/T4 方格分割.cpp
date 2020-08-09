#include <cstdio>
int ans,vis[7][7];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

void dfs(int x,int y) {
	if(x == 0 || x== 6 || y == 0 || y == 6) {
		ans++;
		return ;
	}
	vis[x][y] = 1;  //当前点和对称点标记为访问
	vis[6-x][6-y] = 1;
	for(int i=-0; i<4; i++) {
		int tx = x + dx[i];
		int ty = y + dy[i];
		if(tx >=0 && tx <=6 && ty >=0 && ty <=6 && vis[tx][ty] == 0) {
			dfs(tx,ty);
		}
	}
	vis[x][y] = 0;
	vis[6-x][6-y] = 0;
}

int main() {
	dfs(3,3);
	printf("ans=%d\n",ans/4);
	return 0;
}
