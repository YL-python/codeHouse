#include <iostream>
#include <string>

using namespace std;

int n, m, ans; 
char mp[15][15];
int vis[15][15];

void dfs(int x,int y){
	// 先写出界条件
	if(x<0 || x>=n || y<0 || y>=m || vis[x][y] || mp[x][y]=='#'){
		return ;
	} 
	if(mp[x][y] == 'e'){
		ans++;
		return ; 
	}
	vis[x][y] = 1;
	dfs(x+1, y);
	dfs(x-1, y);
	dfs(x, y+1);
	dfs(x, y-1);
	vis[x][y] = 0;
}

int main(){
	int x,y;
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++){
		scanf("%s",&mp[i]);
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(mp[i][j] == 's'){
				x = i;
				y = j;
			}
		}
	}
	dfs(x,y);
	printf("%d\n",ans);
	
	return 0;
}
/*
5 5
s####
.####
.####
.####
....e

1
*/



























