#include <iostream>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct node {
	int num[4];
	int step;
} first, last;
int vis[11][11][11][11];
queue<node>  q;

void bfs() {
	int i;
	node a,next;
	a = first;
	a.step = 0;
	q.push(a);
	vis[a.num[0]][a.num[1]][a.num[2]][a.num[3]] = true;

	while(!q.empty()) {
		a = q.front();
		q.pop();
		// ����
		if(a.num[0] == last.num[0] && a.num[1] == last.num[1] && a.num[2] == last.num[2] && a.num[3] == last.num[3]) {
			cout << a.step ;
			return ;
		}
		for(i = 0; i < 4; i++) { // + 1
			next = a;
			next.num[i] ++ ;
			if(next.num[i] == 10) {
				next.num[i] = 1;
			}
			if(vis[next.num[0]][next.num[1]][next.num[2]][next.num[3]] == 0) {
				vis[next.num[0]][next.num[1]][next.num[2]][next.num[3]] = 1;
				next.step ++;
				q.push(next);
			}
		}
		for(i = 0; i < 4; i++) { // - 1
			next = a;
			next.num[i] -- ;
			if(next.num[i] == 0) {
				next.num[i] = 9;
			}
			if(vis[next.num[0]][next.num[1]][next.num[2]][next.num[3]] == 0) {
				vis[next.num[0]][next.num[1]][next.num[2]][next.num[3]] = 1;
				next.step ++;
				q.push(next);
			}
		}
		for(i = 0; i < 3; i++) { // ����
			next = a;
			next.num[i] = a.num[i+1]; // ���� ����
			next.num[i+1] = a.num[i];

			if(vis[next.num[0]][next.num[1]][next.num[2]][next.num[3]] == 0) {
				vis[next.num[0]][next.num[1]][next.num[2]][next.num[3]] = 1;
				next.step ++;
				q.push(next);
			}
		}
	}

}

int main() {
	int i,j,t;
	char s1[10],s2[10];
	cin >> s1 >> s2;
	for(i=0; i<4; i++) {
		first.num[i] = s1[i] - '0';
		last.num[i] = s2[i] - '0';
	}
	bfs();
	return 0;
}
/*
����һ�������������Ǵ�-������������������
λ������ɣ�ÿ�����ִ�1��9���б�š�ÿ�ο�
�Զ��κ�һλ���ּ�1���1.����9��1ʱ����
�ֽ���Ϊ1����1��1��ʱ�����ֽ���Ϊ9����Ҳ
���Խ����������֣�ÿһ���ж�����һ����������
��������ʹ����С�Ĳ�����������ע��:�����
�����ֲ������ұߵ��������ڡ�

�����ʽ
��һ��������λ���֣���ʾ�������ĳ�ʼ״̬��
�ڶ���������λ���֣���ʾ���������롣

�����ʽ
���һ����������ʾ��С���衣

1234
2144

2

*/



























