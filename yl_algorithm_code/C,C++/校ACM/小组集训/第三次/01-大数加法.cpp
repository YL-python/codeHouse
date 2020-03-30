#include<iostream>
using namespace std;

int ans[205];
string x,y;

void sum(string x,string y) {
	x = '0' + x;
	y = '0' + y;
	int lenx = x.length();
	int leny = y.length();
	int temp;
	if(lenx > leny) {
		for(int i =0; i<lenx-leny; i++) {
			y='0'+y;
		}
		temp = lenx;
	}else{
		for(int i =0; i<leny-lenx; i++) {
			x='0'+x;
		}
		temp = leny;
	}

	int bit = 0;
	int cnt = 0;
	for(int i=temp-1;i>=0;i--){
		int num1 = x[i] - '0';
		int num2 = y[i] - '0';
		bit = num1 + num2 + bit;
		ans[cnt++] = bit%10;
		bit/=10;
	}

}

int main() {
	cin >> x >> y;
	sum(x,y);
	for(int i=205;i>=0;i--){
		if(ans[i] !=0){
			for(int j = i;j>=0;j--){
				cout<< ans[j];
			}
			break;
		}
		if(i == 0){  // 0 + 0 = 0
			cout << 0;
		}
	}
	return 0;
}
