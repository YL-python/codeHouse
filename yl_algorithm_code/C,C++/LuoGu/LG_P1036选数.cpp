#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int a[25], k, n , ans; 

//bool ss(int x){
//	if(x == 1){
//		return false;
//	}
//	if(x == 2){
//		return true;
//	}
//	int m = int(sqrt(x))+1;
//	for(int i=2;i<=m;i++){
//		if(x % i == 0){
//			return false;
//		}
//	}
//	return true;
//} 

// 2 是素数 
bool ss(int a){
    for(int i=2;i*i<=a;i++)
        if(a%i==0)
            return false;
    return true;
}

// 第 i 个数  count 表示选了几个数   sum表示现在选取数的和 
void dfs(int i,int count, int sum){
	if(i == n){
		if(count == k){
//			cout << sum << endl;
			if(ss(sum)){
				ans++;
			}
		}
		return;
	}
	
	dfs(i + 1, count , sum);
	dfs(i+1, count +1, sum+a[i]);
}

int main(){
	cin >> n >> k;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	
	dfs(0,0,0);
	cout << ans;
	return 0;
}




























