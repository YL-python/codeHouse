#include <iostream>
#include <string>
using namespace std;

/*
��һ�������У��������Ӿ���
��һ�������� n m��ʾ�����С 0<n,m<1000
����ÿ��Ԫ����-1000��1000֮��
�������Ӿ���ĺ�
������
3 3
2 -4 1
-1 2 1
4 -2 2
�����
6
*/

int main() {
	int n,m,ans=-1005;
	int a[1005][1005];
	cin >> n >> m;
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			cin >> a[i][j];
		}
	}

	// ö��
	for(int i = 0; i < n; i++) { // ö���ϱ߽�
		for(int j = i; j < n; j++) { // ö���±߽�
			for(int k = 0; k < m; k++) { // ö����߽�
				for(int l = k; l < m; k++) { // ö���ұ߽�
					int temp = 0;
					for(int p = i; p <= j; p++) { // �� i�е� j��
						for(int q = k; q <= l; q++) { // k�е� l��֮�����
							temp += a[p][q];
						}
					}
					if(temp > ans) {
						ans = temp;
					}
				}
			}
		}
	}
	cout << ans << endl;
	return 0;
}

