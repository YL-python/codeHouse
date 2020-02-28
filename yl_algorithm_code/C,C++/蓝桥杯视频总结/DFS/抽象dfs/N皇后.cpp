#include <iostream>
#include <string>
using namespace std;

// 递归  拆盒子问题 

int ans = 0;
// 标记列和两条对角线 
int col[10], x1[20], x2[20];

bool check(int r, int i){
	// 列和两条对角线都没标记就表示可以放下 
	return !col[i] && !x1[r+i] && !x2[r - i + 8];
}

void dfs(int r){
	
	if(r == 8){
		ans ++;
		return ;
	}
	
	// 对 r 行的每一列进行尝试 
	for(int i=0; i<8; i++){
		// 判断 r 行 i 列 是否可以放下，可以放下就标记并且 递归下一行的情况 
		if(check(r, i)){
			col[i] = x1[r+i] = x2[r - i + 8] = 1;
			dfs(r + 1);
			col[i] = x1[r+i] = x2[r - i + 8] = 0;
		}
	}
} 

int main(){
	
	dfs(0);
	cout << ans << endl;
	
	return 0;
}




























