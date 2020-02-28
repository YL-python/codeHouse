#include <iostream>
#include <string>

using namespace std;

int n;
int count[10005][4];
int x,y;
int ans = -1;

int main(){
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> count[i][0] >> count[i][1] >> count[i][2] >> count[i][3];
	}
	cin >> x >> y;
	int tx,ty;
	for(int i=n-1;i>=0;i--){
		tx = count[i][0]+count[i][2];
		ty = count[i][1]+count[i][3];
		if(x>=count[i][0] && x<=tx && y>=count[i][1] && y<=ty){
			ans = i+1;
			break;
		}
	}
	cout << ans;
	return 0;
}




























