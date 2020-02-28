#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int n,a,b,p;
int vis[2005];
int ans[2005];

int fb(int x){
	// 能大大减少时间复杂度 
	if(vis[x] == 1){  // 访问过了 直接return 结果 
		return ans[x];
	}
	vis[x] = 1;  // 标记为访问了 
	if(x == 1 || x == 2){
		return ans[x] = 1%p;  // 更新结果并返回 
	}
	else{
		return ans[x] = ((a*fb(x-1))%p + (b*fb(x-2))%p) % p;
	}
}

int main(){
	
	scanf("%d%d%d%d", &n, &a, &b, &p);
	printf("%d\n",fb(n));
	return 0;
}
/*
f[n] = a*f[n-1] + b*f[n-2] 
求 f[n] 对 p 取模的结果 

5 2 2 1233
28
*/ 



























