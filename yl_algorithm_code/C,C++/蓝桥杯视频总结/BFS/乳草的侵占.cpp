#include <iostream>
#include <string>
#include <queue>

using namespace std;
typedef pair<int, int> pall;


struct node {
	int x, y;
	node() {}
	node(int _x, int _y) {
		x = _x, y = _y;
	}
};

int n,m,u,v;
char mp[110][110];
int vis[110][110];  // 到当前点需要的天数 
int dx[8] = {1, -1, 0, 0, -1, 1, -1, 1};
int dy[8] = {0, 0, 1, -1, 1, 1, -1, -1};

int bfs() {
	vis[u][v] = 1;
	queue<node> q;
	q.push(node(u, v));
	int ans = -1;
	while( !q.empty()) {
		u = q.front().x;
		v = q.front().y;
		q.pop();
		for(int i=0; i<8; i++) {
			int x = u + dx[i];
			int y = v + dy[i];

			if(x >= 0 && x < n && y>=0 && y<m && mp[x][y]=='.' && vis[x][y] == 0) {
				q.push(node(x,y));
				mp[x][y] = '*';
				// 蔓延到 x,y点需要的时间是 u,v点的时间 + 1
				vis[x][y] = vis[u][v] + 1;
				ans = vis[x][y]>ans ? vis[x][y] : ans;
			}
		}
	}
	return ans - 1;
}

int main() {
	cin >> m >> n >> v >> u;
	u -= 1, v -= 1;
	u = n - u - 1;
	for(int i=0; i<n; i++) {
		cin >> mp[i];
	}
	cout << bfs() << endl;
	return 0;
}
/*
Farmer John -直努力让他的草地充满鲜美多汁的
而又健康的牧草。可惜天不从人愿，他在植物大战
人类中败下阵来。邪恶的乳草已经在他的农场的西
北部份占领了一片立足之地。草地像往常一样，被
分割成一个高度为Y(1≤Y≤100),宽度为
X(1≤X≤100)的直角网格。(1,1) 是左下角
的格(也就是说坐标排布跟一般的 X,Y坐标相
同)。乳草-开始占领了格(Mx, My).
每个星期，乳草传播到已被乳草占领的格子四面八
方的每一个没有很多石头的格(包括垂直与水平相
邻的和对角线上相邻的格)。1周之后，这些新占
领的格又可以把乳草传播到更多的格里面了。
Bessie想要在草地被乳草完全占领之前尽可能的享
用所有的牧草。她很好奇到底乳草要多久才能占领
整个草地。如果乳草在0时刻处于格(Mx, My),
那么还在那个时刻它们可以完全占领入侵整片草地
呢(对给定的数据总是会发生) ?草地由一个图片
表示。'.' 表示草，而'*'表示大石。比如这个
X =4,Y= 3的例子。

....
..*.
.**.

如果乳草一开始在左下角(第1排，第1列)
那么草地的地图将会以如下态势发展:

第0周
....
..*.
M**.

第1周
....
MM*.
M**.

第2周
MMM.
MM*.
M**.

第3周
MMMM
MM*M
M**.

第4周
MMMM
MM*M
M**M

乳草会在4星期后占领整片土地。
输入格式
第一行:四个由空格隔开的整数X,Y , Mx, My.
第2到第Y+1行:数据的第y+1行由X个
字符('.'表示草地，'*' 表示大石)，描述草
地的第Y +2- y行。

输出格式
-个单独的整数表示最后-一个不是大石块的格子被
乳草占领的星期数。

shuru
4 3 1 1
....
..*.
.**.

shucu
4
*/



























