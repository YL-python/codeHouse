#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 10010;
int dp[maxn][2];  // 1 表示和前面组合， 0 表示没有 和前面组合 
int w[maxn]; 
int f[35][35];

int main() {
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		cin >> w[i];
	} 
	dp[1][0] = 0;
	for(int i=2;i<=n;i++){
		// 没和情况下的最高分是 前面情况的最大值 
		dp[i][0] = max(dp[i-1][0], dp[i-1][1]);
		// 和了情况下的分数是  
		dp[i][1] = dp[i-1][0] + w[i] * w[i-1];
	}
	cout << max(dp[n][0], dp[n][1]) << endl;
	return 0;
}
/*
游戏是这样，你可以选择如若干对相邻的珠子，让
他们同时消去。每一对珠子的消失，都会使得总分
数加上两颗珠子相乘的分数。注意，每个珠子只能
消- -次，并且珠子消去以后，还会占位。

8
-9 -5 -4 -2 4 -5 -4 2 
*/ 
