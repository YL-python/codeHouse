#include <iostream>
#include <string>

using namespace std;

int dir[8][2] = {
					{2, 1}, {1, 2}, {-1, 2}, {-2, 1},
					{-2, -1}, {-1, -2}, {1, -2}, {2, -1}
				};
char s[10][10]; 
int f;
int vis[10][10];

bool in(int x,int y){
	return 0<=x && x<10 && 0<=y && y<9;
}

void dfs(int x,int y){
	vis[x][y] = 1;
	if(f){
		return ;
	}
	if(s[x][y] == 'T'){
		f = 1;
		return;
	}
	for(int i=0; i<8; i++){
		int dx = x + dir[i][0];
		int dy = y + dir[i][1];
		if(in(dx,dy) && s[dx][dy] != '#' && !vis[dx][dy]){
			dfs(dx, dy);
		}
	}
	// 找一条解可以不取消标记，因为标记的点走不到终点之后的点都可以不走了
	// 找多组解就要取消标记 
	// vis[x][y] = 0;
}


int main(){
	int x,y;
	for(int i=0; i<10; i++){
		scanf("%s",&s[i]);
	}
	for(int i=0;i<10;i++){
		for(int j=0;j<9;j++){
			if(s[i][j] == 'S'){
				x=i;
				y=j;
			}
		} 
	}
	dfs(x,y);
	if(f){
		printf("YES!");
	}else{
		printf("NO!");
	}
	return 0;
}
/*
.#....#S#
..#.#.#..
..##.#..#
......##.
...T.....
...#.#...
...#.....
...###...
.........
.##......
NO!
*/



























