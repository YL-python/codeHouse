#include <iostream>
#include <string>

using namespace std;



int main() {
	int n;
	int a[105];
	cin >> n;
	for(int i=0; i<=n; i++) {
		cin >> a[i];
	}

	for(int i=0; i<n; i++) {
		if(a[i] == 0) {
			continue;
		}

		if(i == 0) {
			if(a[i] == 1) {

			}
			if(a[i]>1) {
				cout << a[i];
			}
			if(a[i] == -1) {
				cout << "-";
			}
			if(a[i]<-1) {
				cout << a[i];
			}
		} else {
			if(a[i] == 1) {
				cout << "+";
			}
			if(a[i]>1) {
				cout << "+" << a[i];
			}
			if(a[i] == -1) {
				cout << "-";
			}
			if(a[i]<-1) {
				cout << a[i];
			}
		}
		cout << "x";
		if(n-i == 1){
			
		}else{
			cout << "^" << n-i;
		}

	}
	if(a[n] > 0){
		cout << "+" << a[n];
	}
	if(a[n] < 0){
		cout << a[n];
	}

	return 0;
}




























