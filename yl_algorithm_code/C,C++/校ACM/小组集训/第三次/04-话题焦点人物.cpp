#include <iostream>
using namespace std;

int main() {
	int b[105][105]= {0}; // i 有没有被 j提及到 
	int cnt[105]= {0};  // i被提及的次数 
	int maxcnt=-1,hotpeople;
	int n,a,k,temp;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a >> k;
		for(int j=0; j<k; j++) {
			cin >> temp;  // a 提及了 temp
			b[temp][a] = 1;  // temp 被 a 提及了 
			cnt[temp]++;  //  temp 提及次数++ 
		}
	}
	for(int i=0; i<105; i++) {
		if(cnt[i] > maxcnt) {
			maxcnt = cnt[i];
			hotpeople = i;
		}
	}
	cout << hotpeople << endl;
	for(int i=0; i<105; i++) {
		if(b[hotpeople][i]) {
			cout << i << " ";
		}
	}
	return 0;
}
