#include <iostream>
using namespace std;

int gcd(int a,int b) {
	return b?gcd(b,a%b):a;
}

int main () {
	int n;
	cin >> n;
	int ansa=0,ansb=1;
	int a,b;

	for(int i=0; i<n; i++) {
		scanf("%d/%d",&a,&b);
		ansa = ansa * b + a * ansb;
		ansb = ansb * b;
		int x = gcd(ansa,ansb);
		ansa /= x;
		ansb /= x;
	}
	if(ansb == 1) {
		cout << ansa;
	} else {
		cout<< ansa << "/" << ansb;
	}

	return 0;
}
