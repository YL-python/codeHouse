#include <iostream>
using namespace std;

int main() {

	int col,row;
	char c;
	cin >> col >> c;
	row = (col+1) / 2;
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			cout << c;
		}
		cout << endl;
	} 

	return 0;
}
