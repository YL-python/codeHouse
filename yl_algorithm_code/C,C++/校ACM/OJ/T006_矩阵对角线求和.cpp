#include <iostream>
using namespace std;
int main() {
	int n,a[3][3];
	cin >> n;
	for(int k=0; k<n; k++) {
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				cin >> a[i][j];
			}
		}
		cout << a[0][1] + a[1][0] + a[1][2] + a[2][1] << endl;
	}

	return 0;
}
