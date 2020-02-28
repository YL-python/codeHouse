#include <iostream>
#include <string>
// 思路 看看王子 和公主可以到哪些点 看看有没有重复
using namespace std;

int n,m;
char mp[105][105];
int vis[105][105][2];

void dfs(int x, int y, int d) {
	if(x<0 || x>=n || y<0 || y>=m || vis[x][y][d] || mp[x][y]=='#') {
		return ;
	}
	vis[x][y][d] = 1;

	dfs(x-(2-d), y, d);
	dfs(x+(2-d), y, d);
	dfs(x, y-(2-d), d);
	dfs(x, y+(2-d), d);
}

int main() {

	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++){
		scanf("%s",mp[i]);
	}
	int x,y;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(mp[i][j] == 'w') {
				x=i;
				y=j;
			}
		}
	}
	dfs(x,y,0);  // 0 表示王子
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(mp[i][j] == 'g') {
				x=i;
				y=j;
			}
		}
	}
	dfs(x,y,1);  // 1 表示公主
	int f=0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(vis[i][j][0] && vis[i][j][1]) {
				f = 1;
			}
		}
	}
	if(!f){
		printf("no\n");
	}else{
		printf("yes\n");
	}
	return 0;
}
/*
一天，蒜头君梦见自己当上了王子，但是不幸的
是，自己的公主被可恶的巫婆抓走了。于是蒜头君
动用全国的力量得知，自己的公主被巫婆抓进一个
迷宫里面。由于全国只有蒜头君自己可以翻越迷宫
外的城墙，蒜头君使自己-人走上的拯救自己公主
的路途。碰巧的是巫婆出去了，迷宫也不大。蒜头
君可以直接和公主对话，于是两个人便开始相互靠
近。蒜头君救公主心切，1 次必须沿着一个方向走
两步(有 可能跨越迷宫的墙) ;公主柔弱，1 次只
能走一步。问在这个迷宫中，蒜头君是否可以救出
公主(蒜头君和公主相遇后，就能背着公主逃出迷
宫了)。

输入格式.
第一行输入两个整数n(1≤n≤100),
m(1≤m≤100)表示迷宫的行和列。.
然后有一-个n x m的地图，地图
由'.'、'#'、 'w'、'g'这四个部分组
成。'.' 表示可以通行的路，'#' 表示迷宫的
墙，'w' 表示王子开始所在的位置，'g' 表示公主
开始所在的位置。
输出格式
输出王子是不可以救出自己的公主，如果能救出则
输出"yes"，否则输出"no"。

1 8
w....#.g

yes

*/



























