#include <iostream>
using namespace std;

long long a;

int main () {
	cin >> a;
	if(a <= 2) {
		cout << a;
	} else {  // 大于2 
		if(a%2 == 1) { // 基数 
			cout << a * (a-1) * (a-2);
		}else{  // 偶数 
			if(a % 3 == 0){
				cout << (a-1) * (a-2) * (a-3);
			} else{
				cout << a * (a-1) * (a-3);
			}
		}
	}
	return 0;
}
/*
已知一个正整数N，问从1~N中任选出三个数，他们的最小公倍数最大可以为多少。
暴力 n3  数据范围10 6  爆时间
最大，越往后越大 
*/
