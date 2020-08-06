#include <iostream>
using namespace std;

int n,a[105];
// 首项 末项 1 -1 特判  在次数为 1 的时候又要特判

int main() {
	cin >> n;
	for(int i=0; i<=n; i++) {
		cin >> a[i];
	}

	for(int i=0; i<=n; i++) {
		if(a[i] == 0) {
			continue;
		}
		if(a[i] < 0) {
			if(i == n) {
				cout << a[i];
			} else {
				if(a[i] == -1) {
					if(n-i == 1) {
						cout << "-x";
					} else {
						cout << "-x^" << n-i;
					}
				} else {
					if(n-i == 1) {
						cout << a[i] << "x";
					} else {
						cout << a[i] << "x^" << n-i;
					}
				}
			}
		}
		if(a[i] > 0) {
			if(i==0) {
				if(a[i] == 1) {
					if(n-i == 1) {
						cout << "x";
					} else {
						cout << "x^" << n-i;
					}
				} else {
					if(n-i == 1) {
						cout << a[i] << "x";
					} else {
						cout << a[i] << "x^" << n-i;
					}
				}
			} else if(i == n) {
				cout <<"+"<< a[i];
			} else {
				if(a[i] == 1) {
					if(n-i == 1) {
						cout <<"+"<< "x";
					} else {
						cout <<"+"<< "x^" << n-i;
					}
				} else {
					if(n-i == 1) {
						cout <<"+"<< a[i] << "x";
					} else {
						cout <<"+"<< a[i] << "x^" << n-i;
					}

				}
			}
		}
	}
	return 0;
}
