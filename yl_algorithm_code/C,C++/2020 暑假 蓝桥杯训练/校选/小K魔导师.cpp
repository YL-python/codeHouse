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

	// �����һ�е����
	if(y != 1) {
		y = 1;
	}
	// �����һ��
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
	// ����ѭ����
	while(temp != n*m) {
		// �����ƶ����������ƶ�
		// �����ƶ��� û���ƶ�����������һ��
		if(x+1 <= n && fanxiang == 1) {
			x+=1;  // ������
			// ��һ��  // �ж�����߻����ұ�
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
				// ��ʼ�� x ��
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

