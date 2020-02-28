#include <iostream>
#include <string>
using namespace std;

/*
求一个矩阵中，和最大的子矩阵
第一行两个数 n m表示矩阵大小 0<n,m<1000
矩阵每个元素在-1000到1000之间
输出最大子矩阵的和
样例：
3 3
2 -4 1
-1 2 1
4 -2 2
输出：
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

	// 枚举
	for(int i = 0; i < n; i++) { // 枚举上边界
		for(int j = i; j < n; j++) { // 枚举下边界
			for(int k = 0; k < m; k++) { // 枚举左边界
				for(int l = k; l < m; k++) { // 枚举右边界
					int temp = 0;
					for(int p = i; p <= j; p++) { // 在 i行到 j行
						for(int q = k; q <= l; q++) { // k列到 l列之间遍历
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

