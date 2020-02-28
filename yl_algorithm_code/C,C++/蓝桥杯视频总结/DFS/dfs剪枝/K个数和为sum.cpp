#include <iostream>
#include <string>

using namespace std;

int n,k,sum,ans;
int a[40]; 

void dfs(int i,int cnt,int s){  // 当前第几个数，选了几个数，当前和 

	// 剪枝
	if(cnt > k){
		return;
	} 
	if(s > sum){
		return ;
	}

	// 不剪枝时间复杂度是 O(2的 n 次方) 
	if(i == n){  // ans++ 条件 
		if(cnt == k && s == sum){
			ans ++;
		}
		return ;
	}
	dfs(i + 1, cnt+1, s+a[i]);
	dfs(i + 1, cnt, s);
}

int main(){
	n = 30;
	k = 8;
	sum = 200;  // 30个数选 8个数和是 300 
	for(int i=0;i<n;i++){
		a[i] = i+1;
	}
	
	dfs(0,0,0);
	cout << ans << endl;
	
	return 0;
}




























