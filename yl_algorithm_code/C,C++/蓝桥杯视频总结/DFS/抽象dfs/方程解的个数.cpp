#include <iostream>
#include <string>

using namespace std;

int k[5],p[5]; 
int n,m,ans; 

long long poww(int x, int y){
	int ans=1;
	while(y){
		ans *=x;
		y --;
	}
	return ans;
}

void dfs(int x,int s){  
	if(x == n){   // n��ѭ�� 
		if(s == 0){
			ans ++;
		}
		return ;
	}
	for(int i=1;i<=m;i++){ // ÿ��ѭ���� 1 ~ m 
		dfs(x+1, s+k[x]*poww(i,p[x]));  // ѭ��+1 �� ѭ��Ҫ���еĲ��� 
	}
	
}

int main(){
	cin >> n >> m;
	for(int i=0;i<n;i++){
		cin >> k[i] >> p[i];
	}
	dfs(0,0);
	cout << ans;
	return 0;
}
/*
3
100
1 2
-1 2
1 2

104
*/



























