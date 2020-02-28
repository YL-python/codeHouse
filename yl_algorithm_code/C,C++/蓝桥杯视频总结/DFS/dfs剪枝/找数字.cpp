#include <iostream>
#include <string>

using namespace std;

int n;
bool ok=false;

void dfs(long long x, int cnt){
	if(cnt >= 19){
		return;
	}
	if(ok){
		return;
	}
	if(x % n == 0){
		ok = true;
		cout << x << endl;
		return;
	}
	dfs(x * 10 + 0, cnt + 1);
	dfs(x * 10 + 1, cnt + 1);
}

int main(){
	cin >> n;
	dfs(1,0);
	return 0;
}
/*
给一个数n,让你找出一个只由0, 1组成的十进制
数m，要求这个正整数m可以被n整除。
输入格式
输入-个整数n(1≤n < 200)。
输出格式
对于输入整数n的每一个值，输出m的相应值, .
保证有-个数字长度小于19位的数字。如果有-
个给定值n有多个解，其中任何一个都是可以接受
的。

*/



























