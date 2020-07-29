#include <iostream>
using namespace std;

// 高精度用 temp 
double sn=0.0;
int k;

int main() {
	cin >> k;
	double temp = 0.0;
	while(sn <= k) {
		temp += 1.0;
		sn += 1.0/temp;
	}
	cout << temp;
	return 0;
}
