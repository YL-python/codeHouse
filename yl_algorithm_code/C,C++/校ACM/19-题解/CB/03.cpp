#include <iostream>
using namespace std;

// 吧这个次数定义成全局变量，第一次可以来一个小值来测试 
int N=20190324;

main(){
	int mod = 10000;
	int a,b,c,ans;
	a=1,b=1,c=1; 
	for(int i=4;i<=N;i++){
		ans = (a+b+c) % mod;
		a=b,b=c,c=ans;
	}
	cout << ans << endl;
	return 0;
} 
/*
给定数列 1, 1, 1, 3, 5, 9, 17, …，从第 4 项开始，每项都是前 3 项的和。求
 第 20190324 项的最后 4 位数字。
*/ 
