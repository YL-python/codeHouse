#include <iostream>
#include <string>

using namespace std;

int n;
bool vis[20]; 

void dfs(int cnt, int num){
	if(cnt == n){
		printf("%d\n", num);
		return;
	}
	for(int i = 1;i<=n;++i){  // 当前位置对每一个数字进行尝试 
		if(!vis[i]){
			vis[i] = true;
			dfs(cnt + 1, num*10 + i);
			vis[i] = false;
		}
	}
}

int main(){
	cin >> n;
	int ans = 1;
	for(int i=1;i<=n;++i){
		ans *= i;
	}
	cout << ans << endl;
	dfs(0, 0);
	return 0;
}
/*
全排列  深搜都是全排列  所以贼几把费时间
全排列就可以把所有情况列举出来 

从n个不同元素中任取m(m≤n)个元素，按
照一定的顺序排列起来，叫做从n个不同元素中取
出m个元素的一个排列。当m=n时所有的排
列情况叫全排列。
今天这道题目很简单就是给你一个整数n,计算
[1, n]所有数字的排列组合。

*/



























