#include <iostream>
using namespace std;

int n[10],h,ans;

int main() {
	for(int i=0; i<10; i++) {
		cin >> n[i];
	}
	cin >> h;
	h+=30;
	for(int i=0; i<10; i++) {
		n[i] <=h?ans++:1;
	}
	cout << ans;
	return 0;
}
