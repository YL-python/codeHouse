#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int n;
	float biaozun,w,h;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> h >> w;
		biaozun = (h-100.0) * 1.8;

		if (fabs(biaozun - w) < (biaozun*0.1)) {
			printf("You are wan mei!\n");
		} else if(biaozun>w) {
			printf("You are tai shou le!\n");
		} else {
			printf("You are tai pang le!\n");
		}
	}
	return 0;
}
