#include <iostream>
#include <string>

using namespace std;

int n,k,sum,ans;
int a[40]; 

void dfs(int i,int cnt,int s){  // ��ǰ�ڼ�������ѡ�˼���������ǰ�� 

	// ��֦
	if(cnt > k){
		return;
	} 
	if(s > sum){
		return ;
	}

	// ����֦ʱ�临�Ӷ��� O(2�� n �η�) 
	if(i == n){  // ans++ ���� 
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
	sum = 200;  // 30����ѡ 8�������� 300 
	for(int i=0;i<n;i++){
		a[i] = i+1;
	}
	
	dfs(0,0,0);
	cout << ans << endl;
	
	return 0;
}




























