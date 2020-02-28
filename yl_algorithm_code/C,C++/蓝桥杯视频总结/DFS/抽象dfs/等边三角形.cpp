#include <iostream>
#include <string>

using namespace std;

int n,p[15],sum;
int f,vis[15];

// 制造出了 cnt 根木棍，当前长度和
void dfs(int cnt, int s){
	if(f){
		return;
	}
	if(cnt == 3){
		f = 1;
		return ;
	}
	if(s == sum / 3){
		dfs(cnt+1, 0);
	}
	for(int i=0;i<n;i++){
		if(!vis[i]){
			vis[i] = 1;
			dfs(cnt, s+p[i]);
			vis[i] = 0;
		}
	}
}

int main(){
	
	cin >> n;
	
	for(int i=0;i<n;i++){
		cin >> p[i];
		sum += p[i];
	}
	if(sum %3 != 0){
		printf("no\n");
	}else{
		dfs(0,0);
		if(f){
			printf("yes\n");
		}else{
			printf("no\n");
		}
	}
	return 0;
}
/*
蒜头君手.上有一些小木棍，它们长短不一，蒜头君
想用这些木棍拼出一个等边三角形，井且每根木棍
都要用到。例如， 蒜头君手.上有长度为1, 2, 3,
3的4根木棍，他可以让长度为1, 2的木棍组成
-条边，另外2跟分别组成2条边，拼成-个边长
为3的等边三角形。蒜头君希望你提前告诉他能不
能拼出来，免得白费功夫。

输入格式
首先输入一个整数n(3 <= n <= 10)，表示木棍数
量，接下来输入n根木棍的长度
p(1≤P ≤10000).
输出格式
如果蒜头君能拼出等边三角形，输出"yes"，否则
输出"no" .

5
1 2 3 4 5

yes



*/ 



























