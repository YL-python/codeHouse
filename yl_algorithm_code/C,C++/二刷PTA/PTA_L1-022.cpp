#include<iostream>
#include<string>
using namespace std;

int main() {
	int n,numji=0,numou=0,cnt;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> cnt;
		cnt%2==0 ? numou++ : numji++;
	}
	cout << numji << " " << numou ;
	return 0;
}
