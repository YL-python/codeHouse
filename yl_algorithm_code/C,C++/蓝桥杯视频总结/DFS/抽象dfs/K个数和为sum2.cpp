#include <iostream>
#include <string>

using namespace std;

int n, k, sum, ans;
int a[110], xuan[110];

void dfs(int s,int cnt, int pos){
	if(cnt == k){
		if(s == sum){
			ans ++;
		}
		return;
	}
	if(cnt > k || s > sum){
		return;
	}
	for(int i=pos;i<n;i++){
		if(!xuan[i]){
			xuan[i] = 1;
			dfs(s+a[i], cnt+1, i+1);
			xuan[i] = 0;
		}
	}
}

int main(){
	
	cin >> n >> k >> sum;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	ans = 0;
	dfs(0, 0, 0);
	cout << ans << endl;
	return 0;
}
/*
对于前面 k个数的和的求法，我们除了可以用上面的dfs方法以后，还有-种搜索策略。
之前的方法是每次去抉择是否选择第i个数，现在我们的策略是从剩下的数中选择一个数。 
比如有5个数1,2,3,4,5,如果选择了1,那么剩下2,3, 4, 5四个数;如果选择了2,那么剩下1,3,4,5四个数，
还可以选择....选择....选择....

5 3 9
1 2 3 4 5

2

1 3 5, 3 5 1, 1 5 3 会变成三种情况 

*/



























