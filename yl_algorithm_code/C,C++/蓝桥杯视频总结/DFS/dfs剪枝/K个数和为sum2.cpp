#include <iostream>
#include <string>

using namespace std;

int n,k,sum,ans;
int a[40], xuan[40];

void dfs(int s, int cnt,int pos){  // 事件复杂度是 O(k的 n次方) 
	if(s > sum || cnt > k){
		return;
	}

	if(s == sum && cnt == k){
		ans ++;
	}
	for(int i=pos;i<n;i++){  // pos 控制选择的顺序 
		if(!xuan[i]){
			xuan[i] = 1;
			dfs(s + a[i], cnt+1, i+1);
			xuan[i] = 0;
		}
	}
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




























