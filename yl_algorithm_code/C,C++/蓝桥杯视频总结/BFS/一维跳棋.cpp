#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;
const int N = (1 << 20) * 21 + 5;
bool vis[1 << 20][21];
struct node{
	int s, x;
};
int p[N]; 

int main(){
	int n;
	cin >> n;
	vector<node> a;
	queue <int> q;
	int s1 = (1 << n) - 1;
	int s2 = s1 << n;
	q.push(a.size());
	vis[s1][n] = true;
	a.push_back({s1, n});
	while(!q.empty()){
		int id = q.front();
		q.pop();
		int s = a[id].s, x = a[id].x;
		if(s == s2 && x == n){
			vector<int> ans;
			for(int i=id; i ;i=p[i]){
				ans.push_back(2 * n - a[i].x + 1);
			}
			reverse(ans.begin(), ans.end());
			for(int i=0;i<ans.size(); i++){
				cout << ans[i] << (i%5 == 4 ? "\n" : " " );
			}
			break;
		}
		// 空格左边棋子移动到空格位置 
		if(x < 2*n){
			int ts = s;
			int tx = x + 1;
			if(!vis[ts][tx]){
				q.push(a.size());
				vis[ts][tx] = true;
				p[a.size()] = id;
				a.push_back({ts, tx});
			}
		}
		// 空格右边棋子移动到空格位置 
		if(x > 0){
			int ts = s;
			int tx = x - 1;
			if(!vis[ts][tx]){
				q.push(a.size());
				vis[ts][tx] = true;
				p[a.size()] = id;
				a.push_back({ts, tx});
			}
		}
		// 空格左边棋子跳到空格
		if(x <= 2*n-2 && ((s >> x+1 & 1) ^ (s >> x & 1))){
			int ts = s ^ (3 << x);
			int tx = x + 2;
			if(!vis[ts][tx]){
				q.push(a.size());
				vis[ts][tx] = true;
				p[a.size()] = id;
				a.push_back({ts, tx});
			}
		}
		// 空格右边棋子跳到空格
		if(x >= 2 && ((s >> x-1 & 1) ^ (s >> x-2 & 1))){
			int ts = s ^ (3 << x-2);
			int tx = x - 2;
			if(!vis[ts][tx]){
				q.push(a.size());
				vis[ts][tx] = true;
				p[a.size()] = id;
				a.push_back({ts, tx});
			}
		}
	}
	return 0;
}
/*
--维跳棋是一种在 1x(2N+1)的棋盘上玩的游
戏。一共有N个棋子，其中N个是黑的，N个.
是白的。游戏开始前，N个白棋子被放在- -头,
N个黑棋子被放在另一头，中间的格子空着。在这
个游戏里有两种移动方法是允许的:你可以把一个
棋子移到与它相邻的空格;你可以把一个棋子跳过
一个(仅一个)与它不同色的棋子到达空格。
对于N = 3的情况，棋盘状态依次为:
www BBB
ww WBBB
WwBw BB
WWBwB B
WWB BWB
W BWBWB
 WBWBWB
BW WBWB
BWBW WB
BWBWBW
BWBWB W
BWB BWw
B BWBWW
BB WBWW
BBBW ww
BBB www

对应的空格所在的位置(从左数)为:
3 5 6 4 2 1 3 5 7 6 4 2 3 5 4。


输入一个整数
输出格式
依次输出空格所在棋盘的位置，每个整数间用空格
分隔，每行5个数(每行结尾无空格，最后一行可
以不满5个数;如果有多组移动步数最小的解，输
出第一个数最小的解)

4

4 6 7 5 3
2 4 6 8 9
7 5 3 1 2
4 6 8 7 5
3 4 6 5
*/ 



























