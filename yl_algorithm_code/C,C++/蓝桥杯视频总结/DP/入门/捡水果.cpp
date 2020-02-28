#include <iostream>
using namespace std;
int f[1005][1005];
int inf=100000000;
int main(){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=i;j++){
			cin >> f[i][j];
		}
	}
	int ma = -inf;
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=i;j++){
			f[i][j] += max(f[i-1][j],f[i-1][j-1]);
			if(i == n){
				ma = max(f[i][j],ma);
			}
		}
	}
	if(ma == -inf){
		ma = 0;
	}
	cout << ma << endl;
	return 0;
} 
/*
只能向下或者向右走 
4
3
1 2
6 2 3
3 5 4 1
15
*/
