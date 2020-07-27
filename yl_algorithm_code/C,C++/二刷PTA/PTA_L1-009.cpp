#include<iostream>
using namespace std;

int numup[105],numdown[105],n;
char c;

int gcd(int a,int b) {
	return b?gcd(b,a%b):a;
}

int main() {
	cin >> n;
	int up = 0, down = 1;
	for(int i=0; i<n; i++) {
		cin >> numup[i] >> c >> numdown[i];
		up = up*numdown[i] + numup[i]*down;
		down = down*numdown[i];

		int x = gcd(up,down);
		up /= x;
		down /= x;
	}
	int x = gcd(up,down);
	up = up/x;
	down = down/x;

	if(up == 0) {
		cout<< 0;
		return 0;
	}

	if(up<0) {
		cout<<"-";
		up*=-1;
	}

	if(up>down) {
		int A = up/down;
		if(up%down == 0) {
			cout<<A;
		} else {
			cout<<A<<" "<< up-(A*down)<< "/"<<down;
		}
	} else {
		cout<< up << "/"<<down;
	}
	return 0;
}
