#include <iostream>
#include <string>

using namespace std;

int n,f,p[10005],sum;
int vis[10005];

void dfs(int count, int s, int st){
	if(f){
		return ;
	}
	if(count == 3){
		f = 1;
		return ;
	}
	if(s == sum/3){
		dfs(count+1, 0, 0);
	}
	for(int i=st;i<n;i++){
		if(!vis[i]){
			vis[i] = 1;
			dfs(count , s+p[i] ,i+1);
			vis[i] = 0;
		}
	}
}

int main(){
	
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> p[i];
		sum += p[i];
	}
	if(sum %3 != 0){
		printf("no\n");
	}else{
		dfs(0,0,0);
		if(f){
			printf("yes\n");
		}else{
			printf("no\n");
		}
	}
	
	return 0;
}




























