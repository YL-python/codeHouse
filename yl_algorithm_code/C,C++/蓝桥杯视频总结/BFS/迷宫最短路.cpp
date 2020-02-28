#include <iostream>
#include <string>
#include <queue> 

using namespace std;
int n,m;
string maze[110];
bool vis[110][110];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

bool in(int x, int y){
	return x >=0 && x<n && y>=0 && y<m;
} 

struct node{
	int x,y,d; // 位置和 步数 
	node(int xx, int yy, int dd){
		x = xx;
		y = yy;
		d = dd;
	}
};

int bfs(int sx, int sy){
	queue<node> q;
	q.push(node(sx, sy, 0));
	vis[sx][sy] = true;  // 标记当前点访问过了 
	while(! q.empty()){
		node now = q.front();
		q.pop();
		for(int i=0;i<4;i++){
			int tx = dx[i] + now.x;
			int ty = dy[i] + now.y;
			if(in(tx,ty) && maze[tx][ty]!='*' && vis[tx][ty] != true){
				if(maze[tx][ty] == 'T'){
					return now.d + 1;
				}else{
					vis[tx][ty] = true;
					q.push(node(tx,ty,now.d+1));
				}
			}
		}
	} 
	return -1;
} 

int main(){
	cin >> n>> m;
	for(int i=0;i<n;i++){
		cin >> maze[i];
	}
	int x,y;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(maze[i][j] == 'S'){
				x=i, y=j;
			}
		}
	}
	cout << bfs(x, y) << endl;
	
	return 0;
}
/*
5 6
....S*
.**...
.*..*.
*..**.
.T....

7
*/



























