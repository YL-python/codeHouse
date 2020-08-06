#include <iostream>
using namespace std;

// 都这样了 一看就是有规律的
/*
f[1]=1
f[2]=2=f[1]+1
f[3]=2=f[1]+1
f[4]=4=f[1]+f[2]+1
f[5]=4=f[1]+f[2]+1

f[n]=f[1]+f[2]+f[3]+ ... +f[n/2]+1;
*/
int f[1005],n;
int main() {
	cin >> n;
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=i/2; j++) {
			f[i] += f[j];
		}
		f[i] ++;
	}
	cout << f[n];
	return 0;
}
