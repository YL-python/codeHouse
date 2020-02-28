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
	// ��ż�Լ�֦ 
	if((sx + sy + ex + ey + T)%2 !=0 ){ // ͬɫ��Ҫż����  ��ͬɫ��Ҫ������ 
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
��һ��n x m��С���Թ��������ַ�'S'��ʾ��㣬�ַ�'D'��ʾ���ڣ��ַ�'x'��ʾǽ�ڣ��ַ�'.' ��ʾƽ�ء�����Ҫ
��'S'�����ߵ�'D'��ÿ��ֻ���������������ڵ�λ���ƶ������Ҳ����߳���ͼ��Ҳ�����߽�ǽ�ڡ�
ÿ���ƶ�����1ʱ�䣬�߹�·�������ݣ���˲����߻�ͷ·����ԭ�ز�����������֪���ڵĴ��Ż���Tʱ��򿪣��ж���0ʱ
����������ܷ������Թ���
���ݷ�Χn,m��10,T��50��

4 4 5
S.X.
..X.
..XD
....

NO
*/ 



























