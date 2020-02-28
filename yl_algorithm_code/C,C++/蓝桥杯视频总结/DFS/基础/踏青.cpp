#include <iostream>
#include <string>

using namespace std;

int dir[4][2] = {{-1,0},{0,-1},{1,0},{0,1}};
int vis[105][105];
char mp[105][105];
int cnt;
int n,m;

void dfs(int x, int y){
	vis[x][y] = 1;
	for(int i=0; i<4; i++){
		int dx,dy;
		dx = x + dir[i][0];
		dy = y + dir[i][1];
		if(0<=dx && dx<n && dy>=0 && dy<m && !vis[dx][dy] && mp[dx][dy] =='#'){
			dfs(dx, dy);
		}
	}
}

int main(){
	
	cin >> n >> m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin >> mp[i][j];
		}
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(!vis[i][j] && mp[i][j] == '#'){
				dfs(i, j);
				cnt++;
			}
		}
	}
	cout << cnt << endl;
	return 0;
}
/*
5 6
.#....
..#...
..#..#
...##.
.#....

5 
*/



























