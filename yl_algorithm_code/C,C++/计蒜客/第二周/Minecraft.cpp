#include <iostream>
using namespace std;
int n,c,k,g,s;
int _min=6001;
int main() {
	cin >> n;
	
	// 枚举 +长方体表面积计算公式
	for(c=1; c<=n; c++) {
		for(k=1; k<=n; k++) {
			if(n%c==0 && n%k==0 && n%(c*k)==0) {
				g = n / (c*k);
				s = (c*k + k*g+ c*g)*2;
				_min = _min > s ? s : _min;
			}
		}
	}
	cout << _min;
	return 0;
}
