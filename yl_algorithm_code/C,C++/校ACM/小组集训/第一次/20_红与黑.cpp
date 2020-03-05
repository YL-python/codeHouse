#include <iostream>
using namespace std;

char map[25][25];
int l,h; // h 是行
int ans = 0;

void dfs(int i,int j) {
	map[i][j] = '#';
	ans++;
	if(i-1 >=0 && map[i-1][j] == '.') {
		dfs(i-1,j);
	}
	if(i+1 <h && map[i+1][j] == '.') {
		dfs(i+1,j);
	}
	if(j-1 >=0 && map[i][j-1] == '.') {
		dfs(i,j-1);
	}
	if(j+1 <l && map[i][j+1] == '.') {
		dfs(i,j+1);
	}
}

int main () {

	cin >> l >> h;
	for(int i=0; i<h; i++) {
		for(int j=0; j<l; j++) {
			cin >> map[i][j];
		}
	}

	for(int i=0; i<h; i++) {
		for(int j=0; j<l; j++) {
			if(map[i][j] == '@') {
				dfs(i,j);
			}
		}
	}
	cout << ans;
	return 0;
}
/*
最简单的 dfs情况 
*/
