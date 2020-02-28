#include <iostream>
#include <string>

using namespace std;

int n,sum = 0,s1;
int le[4], a[21],b[21];
bool ok ;

void dfs(int x,int j){
	if(x == 4){
		ok = 1;
		return ;
	}
	if(ok){
		return ;
	}
	if(le[x] > s1){
		return ;
	}
	if(le[x] == s1){ // 可行性剪枝 
		dfs(x+1,1);
	}else{
		for(int f=j;f<=n;f++){  // 有序全排列 
			if(b[f] == 0){
				b[f] = 1;
				le[x] += a[f];
				dfs(x, f+1);
				le[x] -= a[f];
				b[f] = 0;
			}
		} 
	}
}

int main(){
	cin >> n;
	for(int i=1;i<=n;i++){
		cin >> a[i];
		sum += a[i];
	}
	s1 = sum / 4;
	if(sum % 4 != 0){
		cont << "NO!";
		return 0;
	}
	dfs(1,1);
	if(ok){
		cout << "YES!";
	}else{
		cout << "NO!";
	}
	
	
	return 0;
}




























