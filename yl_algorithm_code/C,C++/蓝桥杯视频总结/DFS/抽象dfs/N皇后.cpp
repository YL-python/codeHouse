#include <iostream>
#include <string>
using namespace std;

// �ݹ�  ��������� 

int ans = 0;
// ����к������Խ��� 
int col[10], x1[20], x2[20];

bool check(int r, int i){
	// �к������Խ��߶�û��Ǿͱ�ʾ���Է��� 
	return !col[i] && !x1[r+i] && !x2[r - i + 8];
}

void dfs(int r){
	
	if(r == 8){
		ans ++;
		return ;
	}
	
	// �� r �е�ÿһ�н��г��� 
	for(int i=0; i<8; i++){
		// �ж� r �� i �� �Ƿ���Է��£����Է��¾ͱ�ǲ��� �ݹ���һ�е���� 
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




























