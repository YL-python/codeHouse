#include <iostream>
using namespace std;

int main () {
	int a,b,c;
	int n;
	cin >> n;
	int ans = 0,cnt = 0;
	for(a=1; a<=n; a++) {
		for(b=1; b<=n; b++) {
			for(c=1; c<=n; c++) {
				if((a+b) % 2 == 0 && (b+c)%3 == 0 && (a+b+c) % 5 == 0){
					cnt = a+b+c;
					if(cnt > ans){
						ans = cnt;
					}
				}
			}
		}
	}
	cout << ans;
	return 0;
}
/*

*/
