#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int n,a,b,p;
int vis[2005];
int ans[2005];

int fb(int x){
	// �ܴ�����ʱ�临�Ӷ� 
	if(vis[x] == 1){  // ���ʹ��� ֱ��return ��� 
		return ans[x];
	}
	vis[x] = 1;  // ���Ϊ������ 
	if(x == 1 || x == 2){
		return ans[x] = 1%p;  // ���½�������� 
	}
	else{
		return ans[x] = ((a*fb(x-1))%p + (b*fb(x-2))%p) % p;
	}
}

int main(){
	
	scanf("%d%d%d%d", &n, &a, &b, &p);
	printf("%d\n",fb(n));
	return 0;
}
/*
f[n] = a*f[n-1] + b*f[n-2] 
�� f[n] �� p ȡģ�Ľ�� 

5 2 2 1233
28
*/ 



























