#include <iostream>
using namespace std;

int jiechen(int x){
	int sum=1;
	for(int i=1;i<=x;i++){
		sum *= i;
	}
	return sum;
}

int main() {
	int n;
	cin >> n;
	int sum=0;
	for(int i=1;i<=n;i++){
		sum += jiechen(i);
	}
	cout << sum;

	return 0;
}
