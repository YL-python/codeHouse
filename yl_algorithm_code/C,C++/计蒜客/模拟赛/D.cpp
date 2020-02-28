#include <iostream>
using namespace std;
int a[35] ;
int ans, temp, n;


void dfs(int x, int cnt, int type){
	if(type ==0 && i == n){
		if(cnt > ans){
			ans = cnt;
		}
		return ;
	}
	if(type ==1 && i == n-3){
		if(cnt > ans){
			ans = cnt;
		}
		return ;
	}
	for(int i=x;i<=30;i++){
		if(a[i] > 3){
			a[i] -= 3;
			dfs(i,cnt+1,0);
			a[i] += 3;
		}
	}
}

int main(){
	cin >> n;
	for(int i=1;i<=n;i++){
		cin >> a[i];
	}
	dfs(1,0,0);
	cout << ans;
	return 0;
} 
