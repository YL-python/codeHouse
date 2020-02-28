#include <iostream>
#include <string>

using namespace std;

int n,m;
int ans = 100000;
string maze[110];
bool vis[110][110];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};

bool in(int x,int y){
	return 0<=x && x<n && 0<=y && y<m;
}

void dfs(int x, int y,int step){
	
	if(step >= ans){
		return;
	}
	
	if(maze[x][y] == 'T'){
		ans = step;  // 有剪枝可以直接这样写 
		return ;
	}
	vis[x][y] = 1;
	for(int i=0;i<4;i++){
		int tx = x + dx[i];
		int ty = y + dy[i];
		if(in(tx,ty) && maze[tx][ty]!='*' && !vis[tx][ty]){
			dfs(tx, ty, step+1);
		}
	}
	vis[x][y] = 0;
}

int main(){
	cin >> n >> m;
	for(int i=0;i<n;i++){
		cin >> maze[i];
	}
	int x,y; 
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(maze[i][j] == 'S'){
				x = i;
				y = j;
			}
		}
	}
	dfs(x, y, 0);
	cout << ans;
	
	return 0;
}
/*
3 4
S**.
....
***T

5
*/



























