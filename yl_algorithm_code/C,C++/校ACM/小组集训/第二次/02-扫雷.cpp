#include <iostream>
using namespace std;

int n,m;
char map[105][105];

// °Ë¸ö·½Î»
int tx[8] = {-1,-1,-1,0,0,1,1,1};
int ty[8] = {-1,0,1,-1,1,-1,0,1};

int dfs(int x,int y) {
	int ans = 0;
	for(int i=0; i<8; i++) {
		int dx = x + tx[i];
		int dy = y + ty[i];
		if(0<=dx && dx<n && 0<=dy && dy<m && map[dx][dy] == '*'){
			ans++;
		}
	}
	return ans;
}

int main() {
	cin >> n>> m;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			cin >> map[i][j];
		}
	}
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(map[i][j] == '*') {
				cout << '*';
			} else {
				cout << dfs(i,j);
			}
		}
		cout << endl;
	}

	return 0;
}
