#include <iostream>
using namespace std;

int n,sum = 0,temp=1;

int main() {
	cin >> n;
	for(int i=1;i<=n;i++){
		temp = 1;
		for(int j=1;j<=i;j++){
			temp *= j;
		}
		sum += temp;
	}
	cout << sum;
	return 0;
}
