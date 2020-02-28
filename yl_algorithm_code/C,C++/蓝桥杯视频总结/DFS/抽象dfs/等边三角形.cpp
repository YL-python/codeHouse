#include <iostream>
#include <string>

using namespace std;

int n,p[15],sum;
int f,vis[15];

// ������� cnt ��ľ������ǰ���Ⱥ�
void dfs(int cnt, int s){
	if(f){
		return;
	}
	if(cnt == 3){
		f = 1;
		return ;
	}
	if(s == sum / 3){
		dfs(cnt+1, 0);
	}
	for(int i=0;i<n;i++){
		if(!vis[i]){
			vis[i] = 1;
			dfs(cnt, s+p[i]);
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
		dfs(0,0);
		if(f){
			printf("yes\n");
		}else{
			printf("no\n");
		}
	}
	return 0;
}
/*
��ͷ����.����һЩСľ�������ǳ��̲�һ����ͷ��
������Щľ��ƴ��һ���ȱ������Σ�����ÿ��ľ��
��Ҫ�õ������磬 ��ͷ����.���г���Ϊ1, 2, 3,
3��4��ľ�����������ó���Ϊ1, 2��ľ�����
-���ߣ�����2���ֱ����2���ߣ�ƴ��-���߳�
Ϊ3�ĵȱ������Ρ���ͷ��ϣ������ǰ�������ܲ�
��ƴ��������ð׷ѹ���

�����ʽ
��������һ������n(3 <= n <= 10)����ʾľ����
��������������n��ľ���ĳ���
p(1��P ��10000).
�����ʽ
�����ͷ����ƴ���ȱ������Σ����"yes"������
���"no" .

5
1 2 3 4 5

yes



*/ 



























