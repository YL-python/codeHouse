#include <iostream>
using namespace std;

string x,y;
int ans[205];

void sub(string x,string y) {
	int lenx = x.length();
	int leny = y.length();
	if(lenx > leny) {
		for(int i =0; i<lenx-leny; i++) {
			y='0'+y;
		}
	}

	int bit = 0;
	int cnt = 0;
	// bit = 1时，说明借位了，当bit = 0时，说明并未借位
	for(int i=lenx-1;i>=0;i--){
		int num1 = x[i] - '0';
		int num2 = y[i] - '0';
		num1 -= bit;
		if(num1 >= num2){
			ans[cnt++] = num1 - num2;
			bit = 0;
		}else{
			ans[cnt++] = num1 -num2 + 10;
			bit = 1;
		}
	}
}

int main() {
	cin >> x >> y;
	sub(x,y);	
	for(int i=204;i>=0;i--){
		if(ans[i] != 0){
			for(int j=i;j>=0;j--){
				cout << ans[j];
			}
			break;
		}
		if(i == 0){
			cout << 0;
		}
	}
	return 0;
}
