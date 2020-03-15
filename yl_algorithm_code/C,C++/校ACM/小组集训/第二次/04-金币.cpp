#include <iostream>
using namespace std;

int main() {
	int k;
	cin >> k;
	int cnt = 0 , ans = 0;
	for(int i=1; i<100000; i++) {
		for(int j=1; j<=i; j++) {
			cnt++;
			ans +=i;
			if(cnt == k){
				cout << ans;
				return  0;
			}
		}
	}

	return  0;
}
