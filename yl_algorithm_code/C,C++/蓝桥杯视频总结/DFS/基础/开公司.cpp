#include <iostream>
#include <string>

using namespace std;

int used[15],ans,n;
int task[15][15];

void dfs(int x, int t){
	if(x == n){
		if(t<ans){
			ans = t;
		}
		return ;
	}
	for(int i=0; i<n; i++){  // 搜索第 n 个人 
		if(!used[i]){
			used[i] = 1;
			dfs(x + 1, t+task[x][i]);
			used[i] = 0;
		}
	}
}

int main(){
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			scanf("%d",&task[i][j]); 
		}
	}
	ans = 20000;
	dfs(0, 0); // 第0件任务 , 时间 
	printf("%d\n",ans);
	return 0;
}
/*
2020年，蒜头君自己开了一家拥有N个员工的大
公司。每天，蒜头君都要分配N项工作给他的员
工，但是，由于能力的不同，每个人对处理相同工
作所需要的时间有所差异。
众所周知，蒜头君是- -个非常重视效率的人，他想
知道该如何分配工作，才能使得完成所有工作的时
间总和最小(每个员工只可以被分配到一个工
作)。但是我们也都知道，蒜头君不是一般的懒，
所以蒜头君找到了你，请你拯救一下蒜头君吧!

输入格式
第一行输入-一个整数N,代表有N个员工，员工
编号从1到N(1 <= N≤10)。
接着输入一个N x N的二维矩阵task[N][N],
task[i][j](0≤task[i][j] <= 1000) 指的是第i
项工作如果由j号员工完成所需要的时间。

输出格式
输出一个整数，代表所需要的最少时间总和。

6
10 11 12 11 9 11
11 9 10 13 11 12
12 10 11 10 13 9
9 14 9 10 10 11
10 10 9 11 12 11
10 7 10 10 10 8

54
*/ 



























