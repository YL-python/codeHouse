#include <iostream>
using namespace std;

int a[15],flag=1,ans=0;

int main() {

	for(int i=1; i<13; i++) {
		cin >> a[i];
	}
	int mama=0,zhiji=0;
	for(int i=1; i<13; i++) {
		zhiji+=300;
		zhiji-=a[i];
		if(zhiji < 0) {
			flag=0;
			ans = i;
			break;
		}
		while(zhiji >= 100) {
			zhiji -= 100;
			mama += 100;
		}
	}
	if(flag) {
		cout << mama*1.2 + zhiji;
	} else {
		cout << "-"<< ans;
	}

	return 0;
}
