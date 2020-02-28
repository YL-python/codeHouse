#include <cstdio>
#include <string>

using namespace std;

int n,m;
char maze[110][110];
int vis[110][110];
int dir[4][2] = {{-1,0},{0,-1},{1,0},{0,1}};

bool in(int x,int y){
	return 0<=x && x<n && 0<=y && y<m;
}

bool dfs(int x,int y){
	if(maze[x][y] == 'T'){
		return true;
	}
	vis[x][y] = 1;
	maze[x][y] = 'm';
	for(int i=0;i<4;i++){
		int tx = x + dir[i][0];
		int ty = y + dir[i][1];
		if(in(tx,ty) && maze[tx][ty] != '*' && !vis[tx][ty]){
			if(dfs(tx,ty)){
				return true;
			}
		}
	}
	vis[x][y] = 0;
	maze[x][y] = '.';
	return false;
}

int main(){
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++){
		scanf("%s",maze[i]);
	}
	int x,y;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(maze[i][j] == 'S'){
				x=i,y=j;
				break;
			}
		} 
	}
	if(dfs(x,y)){
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				printf("%c",maze[i][j]);
			} 
			printf("\n");
		}
	}else{
		printf("NO!");
	}
	return 0;
}
/*
shuru:
5 6
....S*
.***..
.*..*.
*.***.
.T....

shucu:
....m*
.***mm
.*..*m
*.***m
.Tmmmm
*/



























