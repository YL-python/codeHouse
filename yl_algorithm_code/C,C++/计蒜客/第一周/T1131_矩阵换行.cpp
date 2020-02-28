#include <iostream>
using namespace std;
int a[6] = {0,1,2,3,4,5};
int x[5][5];
int main(){
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			cin >> x[i][j];
		}
	}
	int n,m,t;
	cin >> n >> m;
	t = a[n];
	a[n] = a[m];
	a[m] = t;
	for(int i=1;i<6;i++){
		for(int j=0;j<5;j++){
			cout << x[a[i]-1][j] << " ";
		}
		cout << endl;
	}
	return 0;
} 
