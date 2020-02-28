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
����ǰ�� k�����ĺ͵��󷨣����ǳ��˿����������dfs�����Ժ󣬻���-���������ԡ�
֮ǰ�ķ�����ÿ��ȥ�����Ƿ�ѡ���i�������������ǵĲ����Ǵ�ʣ�µ�����ѡ��һ������ 
������5����1,2,3,4,5,���ѡ����1,��ôʣ��2,3, 4, 5�ĸ���;���ѡ����2,��ôʣ��1,3,4,5�ĸ�����
������ѡ��....ѡ��....ѡ��....

5 3 9
1 2 3 4 5

2

1 3 5, 3 5 1, 1 5 3 ����������� 

*/



























