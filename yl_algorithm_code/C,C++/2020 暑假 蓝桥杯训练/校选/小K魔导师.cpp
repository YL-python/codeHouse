#include<iostream>
#include<algorithm>
using namespace std;

int vis[105][105];

void fun(int n, int m,int x,int y) {
	int temp = 0;
	int fanxiang = 1;  // 1 up  0 down
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=m; j++) {
			vis[i][j] = 0;
		}
	}
	vis[x][y] = 1;
	temp ++;
	if(temp == n*m) {
		cout << x << " " << y;
	} else {
		cout << x << " " << y << endl;
	}

	// 处理第一行的情况
	if(y != 1) {
		y = 1;
	}
	// 输出第一行
	for(int i=1; i<=m; i++) {
		if(vis[x][i] == 0) {
			vis[x][i] = 1;
			temp ++;
			if(temp == n*m) {
				cout << x << " " << y;
			} else {
				cout << x << " " << y << endl;
			}
			y = i;
		} else {
			continue;
		}
	}
	// 无线循环走
	while(temp != n*m) {
		// 向上移动还是向下移动
		// 向上移动且 没有移动道了最上面一行
		if(x+1 <= n && fanxiang == 1) {
			x+=1;  // 向上走
			// 走一行  // 判断在左边还是右边
			if(y == 1) {
				for(int i=1; i<=m; i++) {
					cout << x << " " << i << endl;
					vis[x][i] = 1;
					temp ++;
					if(temp == n*m) {
						cout << x << " " << y;
					} else {
						cout << x << " " << y << endl;
					}
					y = i;
				}
			} else if(y == m) {
				for(int i=m; i>=1; i--) {
					cout << x << " " << i << endl;
					vis[x][i] = 1;
					temp ++;
					if(temp == n*m) {
						cout << x << " " << y;
					} else {
						cout << x << " " << y << endl;
					}
					y = i;
				}
			}
		} else {
			fanxiang = 0;
		}
		if(fanxiang == 0) {
			int flag = 0;
			for(int i=x; i>=1; i--) {
				if(vis[i][y] == 0) {
					flag = i;
					break;
				}
			}
			if(flag != 0) {
				x = flag;
				// 开始走 x 层
				if(y == 1) {
					for(int i=1; i<=m; i++) {
						cout << x << " " << i << endl;
						vis[x][i] = 1;
						temp ++;
						if(temp == n*m) {
							cout << x << " " << y;
						} else {
							cout << x << " " << y << endl;
						}
						y = i;
					}
				} else if(y == m) {
					for(int i=m; i>=1; i--) {
						cout << x << " " << i << endl;
						vis[x][i] = 1;
						temp ++;
						if(temp == n*m) {
							cout << x << " " << y;
						} else {
							cout << x << " " << y << endl;
						}
						y = i;
					}
				}
			}
		}
	}
}

int main() {
	int t;
	cin >> t;
	int n,m,x,y;
	for(int i=0; i<t; i++) {
		cin >> n >> m >> x >> y;
		fun(n,m,x,y);
	}
	return 0;
}

