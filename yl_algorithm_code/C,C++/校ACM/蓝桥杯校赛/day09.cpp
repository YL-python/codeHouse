#include <iostream>
#include <string>
using namespace std;

int main(){
	int n,a[1005];
	a[0] = 1;
	cin>>n;
	for(int i=1;i<1005;i++){
		a[i] = (a[i-1] + i-1) % 10000;
	}
	
//	for(int i=1;i<n;i++){
//		cout<<"a["<<i<<"] = "<<a[i]<<endl;
//	}
	cout << a[n];
	return 0;
}
/*
自己纸上写出前五个找规律 
f[1] = 1
f[2] = 2 = f[1]+1
f[3] = 4 = f[2]+2
f[4] = 7 = f[3]+3
f[5] = 11 = f[4]+4
...
 f[n] = f[n-1]+n-1
*/
