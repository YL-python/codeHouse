#include <iostream>
#include <string>

using namespace std;

int g[20][20];
bool vis[20];
int ans = 1000000;
int n; 

// u 表示我们在那个城市  cnt表示经过了几个城市  sum表示花费 
void dfs(int u, int cnt, int sum){
	if(sum > ans){
		return ;
	}
	if(cnt == n){
		ans = min(ans , sum+g[u][1]);
		return ;
	}
	vis[u] = 1;
	for(int i=1;i<=n;i++){
		if(!vis[i]){
			dfs(i, cnt+1, sum+g[u][i]);
		}
	}
	vis[u] = 0;
}

int main(){
	cin >> n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cin >> g[i][j];
		}
	}
	dfs(1,1,0);
	cout << ans;
	return 0;
}
/*
马上就要放寒假了，蒜头君已经辛勤的工作-年
了，打算和家人一起出去旅游放松放松。有经验的
人一定知道，出去旅游前一定要有详细的旅行规
划。蒜头君打算旅游n个城市，但并不是每条路线
的花费都是一样的。蒜头君是一个勤俭节俭的人，
他就在想怎么把所有的城市旅游一遍花费最小呢?
(蒜头君不喜欢重复旅游同-个城市，也就是说已
到达过的城市蒜头君是不会再次光临的)

输入格式
第一行输入-一个整数n(1≤n≤15)， 表示有n
个城市。
接下来有一个n X n的矩形，表示每两个城市之
间的火车花费，每两个城市之间的花费不会超过
10000.

输出格式
输出- -个整数，表示从1号城市把所有景点旅游-
遍并且回到1号城市的最小花费。

4
0 1 1 1
1 0 2 1
5 5 0 6
1 1 3 0

8

*/ 



























