#include <iostream>
using namespace std;

int x1,x2,temp,cnt,ans;

int main() {

	for(int i=1; i<=7; i++) {
		cin >> x1 >> x2;
		temp = x1 + x2;
		if( temp > 8 ) {
			if(temp > cnt) {
				cnt = temp;
				ans = i;
			}
		}
	}
	cout << ans;

	return 0;
}
