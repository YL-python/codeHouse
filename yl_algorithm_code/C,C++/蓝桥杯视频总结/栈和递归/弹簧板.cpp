#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n;
int a[205],b[205]; 
int ans[205];
int vis[205];

int f(int x){
	if(x >= n){
		return 0;
	}
	if(vis[x]){
		return ans[x];
	}
	vis[x] = 1;
	return ans[x] = min(f(x+a[x]),f(x+b[x])) + 1;
}

int main(){
	
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	for(int i=0;i<n;i++){
		scanf("%d",&b[i]);
	}
	printf("%d\n",f(0));
	
	return 0;
}
/*
有一个小球掉落在一串连续的弹簧板上，小球落到
某一个弹簧板后，会被弹到某-个地点，直到小球
被弹到弹簧板以外的地方。
假设有n个连续的弹簧板，每个弹簧板占一个单位
距离。第i个弹簧板能选择把小球向前弹a[i]个距
离，或者向前弹b[i]个距离。比如位置1的弹簧能
让小球前进2个距离到达位置3.
现在小球掉到了1号弹簧板上面，请你帮忙计算小
球最少会被弹起多少次，才会弹出弹簧板。1号弹
簧板也算一次。
输入格式
第一个行输入-个n代表-共有n(1≤n≤200)
个弹簧板。
第二行输入n个数字，中间用空格分开。第i个数
字a[i](0< a[i] ≤30)代表第i个弹簧板可以让
小球移动的距离。
第三行输入n个数字，中间用空格分开。第i个数
字b[i](0< b[i] ≤30)代表第i个弹簧板可以让
小球移动的距离。
输出格式
输出一个整数，表示小球被弹起的最小次数。

*/ 



























