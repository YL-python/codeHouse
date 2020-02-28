#include <iostream>
#include <string>
#include<vector>

using namespace std;

vector<int> son[100005];  // 用vector 来写图论的邻接表 
int f[100005];
int ans[100005];

int dfs(int u){
	int ret = 0;
	for(int i=0;i<son[u].size();i++){
		ret += dfs(son[u][i]);
	}
	ans[u] = ret;  // ans 表示我有多少个儿子 
	return ret + 1;  // ret 表示我和我的的后代有多少个 
}

int main(){
	
	int n,x,y,u;
	scanf("%d",&n);
	for(int i=0; i<n-1; i++){ // 最后一个人不会有儿子 
		scanf("%d%d",&x,&y); 
		son[x].push_back(y);
		f[y] = 1; // 表示 y 已经作儿子了 
	} 
	for(int i=1;i<=n;i++){
		if(!f[i]){
			u = i;
			break;
		}
	}
	dfs(u);
	for(int i=1;i<=n;i++){
		printf("%d\n",ans[i]);
	}
	return 0;
}
/*
这一天蒜头君拿到了自己家的家谱，蒜头君便想知
道，在自己家的家谱中，每位祖先有多少直系后代
(直系后代包括他的孩子和他孩子的直系后代) .
但是家族历史源远流长，家谱实在太庞大了，自己
1 个人完全数不过来。热心的你便自告奋勇帮蒜头
君写一个程序，来统计每位祖先有多少直系后代。

输入格式
输入的第 1 行有一个整数n(1 <= n <= 100000),
表示家谱中的总人数。
接下来读入n- 1行，每行有两个整数
x(1≤x≤n),y(1≤y<=n),表示x是y的
父母。
输出格式
输出n行，每行有一一个整数，表示第i个人有多少
个直系后代。

4
1 2
1 4
2 4

3
1
0
0

*/ 



























