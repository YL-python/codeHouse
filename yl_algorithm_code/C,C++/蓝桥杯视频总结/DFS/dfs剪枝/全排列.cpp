#include <iostream>
#include <string>

using namespace std;

int n;
bool vis[20]; 

void dfs(int cnt, int num){
	if(cnt == n){
		printf("%d\n", num);
		return;
	}
	for(int i = 1;i<=n;++i){  // ��ǰλ�ö�ÿһ�����ֽ��г��� 
		if(!vis[i]){
			vis[i] = true;
			dfs(cnt + 1, num*10 + i);
			vis[i] = false;
		}
	}
}

int main(){
	cin >> n;
	int ans = 1;
	for(int i=1;i<=n;++i){
		ans *= i;
	}
	cout << ans << endl;
	dfs(0, 0);
	return 0;
}
/*
ȫ����  ���Ѷ���ȫ����  ���������ѷ�ʱ��
ȫ���оͿ��԰���������оٳ��� 

��n����ͬԪ������ȡm(m��n)��Ԫ�أ���
��һ����˳������������������n����ͬԪ����ȡ
��m��Ԫ�ص�һ�����С���m=nʱ���е���
�������ȫ���С�
���������Ŀ�ܼ򵥾��Ǹ���һ������n,����
[1, n]�������ֵ�������ϡ�

*/



























