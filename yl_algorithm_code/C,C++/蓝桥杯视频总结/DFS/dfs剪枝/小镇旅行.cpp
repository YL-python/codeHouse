#include <iostream>
#include <string>

using namespace std;

bool vis[10][10];
int last[10][10];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};
int n,ans;

bool in(int x, int y){
	return x >=1 && x<=n && y>=1 && y<=n;
} 

// cnt 表示走了多少个格子 
void dfs(int x,int y, int cnt){
	if(x == n && y ==1){
		if(cnt == n*n){
			ans++;
		}
		return ;
	}
	int dir = -1;
	vis[x][y] = true;
	for(int i=0;i<4;i++){
		int ex = x + dx[i];
		int ey = y + dy[i];
		if(in(ex,ey) && !vis[ex][ey]){
			last[ex][ey]--;
			if(last[ex][ey] == 1){
				dir = i;
			}
		}
	}
	
	for(int i=0;i<4;i++){
		if(dir !=-1 && dir != i){
			continue;
		}
		int tx = x+dx[i];
		int ty = y+dy[i];
		if(in(tx,ty) && !vis[tx][ty]){
			int ok = true;
			int r = 0;
			for(int j=0;j<4;j++){
				int ex = tx+dx[j];
				int ey = ty+dy[j];
				if(in(ex,ey) && !vis[ex][ey]){
					if(last[ex][ey] < 2){
						ok = false;
						break;
					}else if(last[ex][ey] == 2){
						r++;
					}
				}
			}
			if(ok && r<=1){
				dfs(tx,ty,cnt+1);
			}
		}
	}
	vis[x][y] = false;
	for(int i=0;i<4;i++){
		int ex = x + dx[i];
		int ey = y + dy[i];
		if(in(ex,ey) && !vis[ex][ey]){
			last[ex][ey]++;
		}
	}
}

int main(){
	cin >> n;
	for(int i=1;i<=n;i++){
		for(int j = 1;j<=n;j++){
			for(int k = 0;k<4;k++){
				int tx = i+dx[k];
				int ty = j+dy[k];
				if(in(tx,ty)){
					last[i][j]++;
				}
			}
		}
	}
	last[n][1]++;
	ans = 0;
	dfs(1,1,1);
	cout << ans ;
	return 0;
}
/*
一个正方形的镇区分为 N*N(1≤N≤7)个小
方块。农场位于方格的左上角，集市位于左下角。
Betsy穿过小镇，从左上角走到左下角，刚好经过
每个方格一次。



*/ 



























