#include <iostream>
using namespace std;
int a[] = {0,0,0,0,0,0,0,1,1,1,1,1},ans,vis[12];

void dfs(int g[3][4],int i,int j) {
	g[i][j] = 0;
	if(i-1 >= 0 && g[i-1][j] == 1) dfs(g,i-1,j);
	if(i+1 <= 2 && g[i+1][j] == 1) dfs(g,i+1,j);
	if(j-1 >= 0 && g[i][j-1] == 1) dfs(g,i,j-1);
	if(j+1 <= 3 && g[i][j+1] == 1) dfs(g,i,j+1);
}

bool check(int path[12]) {
	int g[3][4];
	// һάת��ά
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			if(path[i*4+j] == 1) g[i][j] = 1;
			else g[i][j] = 0;
		}
	}
	// �� g ����ͨ�Լ��
	int cnt = 0;  // ��ͨ��ĸ���
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

void f(int k,int path[12]) {
	if(k == 12) {
		if(check(path)) {
			ans++;
		}
	}
	for(int i=0; i<12; i++) {
		if(i>0 && a[i] == a[i-1] && !vis[i-1]) continue;
		if(!vis[i]) {
			vis[i] = 1;
			path[k] = a[i];
			f(k+1,path);
			vis[i] = 0;
		}
	}
}

int main() {
	int path[12];
	f(0,path);
	cout << ans << endl;
	return 0;
}
