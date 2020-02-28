#include <iostream>
#include <string>

using namespace std;

int n,m, T;
int ok;
string maze[110];
bool vis[110][110];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};

bool in(int x,int y){
	return 0<=x && x<n && 0<=y && y<m;
}

void dfs(int x,int y, int t){
	if(ok){
		return ;
	}
	if(t == T){
		if(maze[x][y] == 'D'){
			ok = 1;
		}
		return ;
	}
	vis[x][y] = true;
	for(int i=0;i<4;i++){
		int tx = x + dx[i];
		int ty = y + dy[i];
		if(in(tx,ty) && maze[tx][ty]!='X' && !vis[tx][ty]){
			dfs(tx, ty, t+1);
		}
	}
	vis[x][y] = false;
}

int main(){
	
	cin >> n >> m >> T;
	for(int i=0;i<n;i++){
		cin >> maze[i];
	}
	int sx,sy,ex,ey; 
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(maze[i][j] == 'S'){
				sx = i;
				sy = j;
			}
			if(maze[i][j] == 'D'){
				ex = i;
				ey = j;
			}
		}
	}
	// 奇偶性剪枝 
	if((sx + sy + ex + ey + T)%2 !=0 ){ // 同色需要偶数步  不同色需要奇数步 
		cout << "NO" << endl;
	}else{
		dfs(sx, sy, 0);
	}
	if(ok){
		cout << "YES" << endl;
	}else{
		cout << "NO" << endl;
	}
	return 0;
}
/*
有一个n x m大小的迷宫。其中字符'S'表示起点，字符'D'表示出口，字符'x'表示墙壁，字符'.' 表示平地。你需要
从'S'出发走到'D'，每次只能向上下左右相邻的位置移动，并且不能走出地图，也不能走进墙壁。
每次移动消耗1时间，走过路都会塌陷，因此不能走回头路或者原地不动。现在已知出口的大门会在T时间打开，判断在0时
间从起点出发能否逃离迷宫。
数据范围n,m≤10,T≤50。

4 4 5
S.X.
..X.
..XD
....

NO
*/ 



























