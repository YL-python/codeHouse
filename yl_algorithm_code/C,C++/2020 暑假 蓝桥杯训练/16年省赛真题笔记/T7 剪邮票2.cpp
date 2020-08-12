#include <cstdio>
#include <algorithm>
using namespace std;
int a[] = {0,0,0,0,0,0,0,1,1,1,1,1},ans;

void dfs(int g[3][4],int i,int j) {
	g[i][j] = 0;
	if(i-1 >= 0 && g[i-1][j] == 1) dfs(g,i-1,j);
	if(i+1 <= 2 && g[i+1][j] == 1) dfs(g,i+1,j);
	if(j-1 >= 0 && g[i][j-1] == 1) dfs(g,i,j-1);
	if(j+1 <= 3 && g[i][j+1] == 1) dfs(g,i,j+1);
}

bool check() {
	int g[3][4];
	// 一维转二维
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			if(a[i*4+j] == 1) g[i][j] = 1;
			else g[i][j] = 0;
		}
	}
	// 对 g 做连通性检测
	int cnt = 0;  // 连通块的个数
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			if(g[i][j] == 1) {
				dfs(g,i,j);
				cnt++;
			}
		}
	}
	return cnt == 1;
}

int main() {
	do {
		if(check()) {
			ans++;
		}
	} while(next_permutation(a,a+12));
	printf("%d\n",ans);
	return 0;
}
