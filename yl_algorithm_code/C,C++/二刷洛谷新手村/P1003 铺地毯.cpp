#include <iostream>
using namespace std;

int n,x,y,ans=-1;
int map[20005][4];

int main() {
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> map[i][0] >> map[i][1] >> map[i][2] >> map[i][3];
	}
	cin >> x >> y;
	for(int i=n-1; i>=0; i--) {
		if(x>=map[i][0] && x<=map[i][0]+map[i][2] && y>=map[i][1] && y<=map[i][1]+map[i][3]) {
			ans = i+1;
			break;
		}
	}
	cout << ans;
	return 0;
}
