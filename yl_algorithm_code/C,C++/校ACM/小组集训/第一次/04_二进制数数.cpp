#include <iostream>
using namespace std;
long long ans = 0;
int a,b;

void tj(int x){
	int y;
	while(x){
		y = x%2;
		x/=2;
		if(y == 1){
			ans ++;
		}
	}
} 
int main (){
	cin >> a >> b;
	for(int i=a;i<=b;i++){
		tj(i);
	}
	cout << ans;
	return 0;
}
/*
　给定L,R。统计[L,R]区间内的所有数在二进制下包含的“1”的个数之和。
　　如5的二进制为101，包含2个“1”。
*/
