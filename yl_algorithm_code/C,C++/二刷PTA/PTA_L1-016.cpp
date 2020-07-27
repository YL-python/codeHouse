#include <iostream>
#include <string>
using namespace std;

int jym[11] = {'1','0','X','9','8','7','6','5','4','3','2'};
int q[17] = {7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2};
int n,temp,jisuanQ;
string sfz;

int main() {
	cin >> n;
	temp = 1;
	for(int i=0; i<n; i++) {
		cin >> sfz;
		jisuanQ = 0;
		for(int j=0; j<17; j++) {
			int cnt = sfz[j] - '0';
			if(cnt >=0 || cnt <=9) {
				jisuanQ += cnt * q[j];
				jisuanQ %= 11;
			} else {
				cout << sfz << endl;
				temp = 0;
				break;
			}
		}
		if(jym[jisuanQ] != sfz[17]) {
			cout << sfz << endl;
			temp = 0;
		}
	}
	if(temp) {
		cout << "All passed";
	}

	return 0;
}
