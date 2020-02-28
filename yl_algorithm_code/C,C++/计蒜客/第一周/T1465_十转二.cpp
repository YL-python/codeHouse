#include <iostream>
using namespace std;
int a[70];
int main() {
	int n;
	for(int i=0; i<5; i++) {
		int cnt = 0;
		cin >> n;
		if(n == 0){
			cout << "0-->0" << endl;
			continue;
		}
		if(n<0) {
			cout << n << "-->-";
			n = -1 * n;
		} else {
			cout << n << "-->";
		}
		while(n) {
			a[cnt++] = n % 2;
			n/=2;
		}
		for(int i=cnt-1; i>=0; i--) {
			cout << a[i];
		}
		cout << "\n";
	}
	return 0;
}
