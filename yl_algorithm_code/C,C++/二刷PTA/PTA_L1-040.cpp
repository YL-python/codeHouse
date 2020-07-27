#include<iostream>
using namespace std;

int main() {
	int n;
	char c;
	double h[15][2];
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> c >> h[i][0];
		if(c == 'M') {
			h[i][1] = h[i][0] / 1.09;
		} else {
			h[i][1] = h[i][0] * 1.09;
		}
	}
	for(int i=0; i<n; i++) {
		printf("%.2lf\n",h[i][1]);
	}
	return 0;
}
