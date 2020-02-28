#include <iostream>
#include <string>

using namespace std;

int n, m, ans, count; 
char mp[1005][1005];
int vis[1005][1005];

void dfs(int x,int y){
	// 先写出界条件
	if(x<0 || x>=n || y<0 || y>=m || vis[x][y] || mp[x][y]=='.'){
		return ;
	} 
	vis[x][y] = 1;
	count ++;
	dfs(x+1, y);
	dfs(x-1, y);
	dfs(x, y+1);
	dfs(x, y-1);
}

int main(){
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++){
		scanf("%s",&mp[i]);
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(mp[i][j] == '#' && !vis[i][j]){
				count = 0;
				dfs(i,j);
				if(count > ans){
					ans = count;
				}
			}
		}
	}
	printf("%d\n",ans);
	
	return 0;
}
/*
# 表示蛋糕，上下左右连续的就可以吃
 
5 6
.#....
..#...
..#..#
...##.
.#....

2 

*/



























