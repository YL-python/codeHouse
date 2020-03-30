#include <iostream>
using namespace std;


int main() {
	int m,s,n;
	int a[205][205];
	int b[205][205];
	cin >> m >> s >> n;
	for(int i=0; i<m; i++) {
		for(int j=0; j<s; j++) {
			cin >> a[i][j];
		}
	}
	
	for(int i=0; i<s; i++) {
		for(int j=0; j<n; j++) {
			cin >> b[i][j];
		}
	}
	
	for(int i=0; i<m; i++) {
		for(int j=0; j<n; j++) {
			int cnt=0;
			for(int k=0;k<s;k++){
				cnt+= a[i][k] * b[k][j];
			}
			cout << cnt << " ";
		}
		cout << endl;
	}

	return 0;
}
/*


*/
