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
		// 出口
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
		for(i = 0; i < 3; i++) { // 交换
			next = a;
			next.num[i] = a.num[i+1]; // 交换 操作
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
现在一个紧急的任务是打开-个密码锁。密码由四
位数字组成，每个数字从1到9进行编号。每次可
以对任何一位数字加1或减1.当将9加1时，数
字将变为1，当1减1的时，数字将变为9。你也
可以交换相邻数字，每一个行动记做一步。现在你
的任务是使用最小的步骤来打开锁。注意:最左边
的数字不与最右边的数字相邻。

输入格式
第一行输入四位数字，表示密码锁的初始状态。
第二行输入四位数字，表示开锁的密码。

输出格式
输出一个整数，表示最小步骤。

1234
2144

2

*/



























