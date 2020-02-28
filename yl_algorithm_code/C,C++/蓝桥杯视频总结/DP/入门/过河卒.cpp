#include <iostream>
using namespace std;
int f[100][100];
int d[100][100];
int cx,cy;
int x[8] = {1,1,2,2,-1,-1,-2,-2};
int y[8] = {2,-2,1,-1,2,-2,1,-1};
int main() {
	int n,m;
	cin >> n>> m >> cx >> cy;
	f[0][0] = 1;
	d[cx][cy] = 1; // 马的控制点
	for(int i=0; i<8; i++) {
		int tx = cx+x[i];
		int ty = cy+y[i];
		if(tx>=0 && tx <=n && ty >= 0 && ty <=m) {
			d[tx][ty] = 1;
		}
	}

	for(int i=0; i<=n; i++) {
		for(int j=0; j<=m; j++) {
			if(d[i][j] == 0) {
				if(i != 0) {
					f[i][j] = f[i][j] + f[i-1][j];
				}
				if(j != 0) {
					f[i][j] = f[i][j] + f[i][j-1];
				}
			}
//			if(d[i][j]){
//				f[i][j] = 0;
//			}
		}
	}
	cout << f[n][m] << endl;
	return 0;
}

/*
	不考虑马的情况s
		F(i,j) = F(i-1,j) + F(i,j-1)
	5 5 2 4
	14
*/
