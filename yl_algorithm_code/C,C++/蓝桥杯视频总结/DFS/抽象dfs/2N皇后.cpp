#include <iostream>
#include <string>
using namespace std;

int mp[10][10]; 
int n, ans;
int vy[10], vd1[20], vd2[20]; 

void dfs(int x, int p){
	if(x == n && p == 2){
		ans ++;
		return;
	}
	if(x == n){
		dfs(0,p+1);
		return ; 
	}

	for(int i=0;i<n;i++){
		if(mp[x][i] != 0 && vy[i] != 3 && vy[i] != p && vd1[x+i]!=3 && vd1[x+i]!=p && vd2[x-i+n]!=3&&vd2[x-i+n]!=p){
			mp[x][i] = 0;
			vy[i] += p;
			vd1[x+i] += p;
			vd2[x-i+n] += p;
			dfs(x+1, p);  // 当前行能放就考虑下一行能不能放 
			mp[x][i] = 1;
			vy[i] -= p;
			vd1[x+i] -= p;
			vd2[x-i+n] -= p;
		}
	}
}

int main(){
	
	cin >> n;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin >> mp[i][j];
		}
	}
	dfs(0,1);
	cout << ans;
	return 0;
}
/*
n * n 个皇后，黑白两个皇后不能在一起，皇后有皇后的规则
棋盘 1 表示可以放，0表示不可以放

4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

2

4
1 0 1 1
1 1 1 1
1 1 1 1
1 1 1 1

0

*/ 



























