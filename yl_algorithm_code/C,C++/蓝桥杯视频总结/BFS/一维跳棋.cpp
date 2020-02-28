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
		// �ո���������ƶ����ո�λ�� 
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
		// �ո��ұ������ƶ����ո�λ�� 
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
		// �ո�������������ո�
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
		// �ո��ұ����������ո�
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
--ά������һ���� 1x(2N+1)�������������
Ϸ��һ����N�����ӣ�����N���Ǻڵģ�N��.
�ǰ׵ġ���Ϸ��ʼǰ��N�������ӱ�����- -ͷ,
N�������ӱ�������һͷ���м�ĸ��ӿ��š�����
����Ϸ���������ƶ������������:����԰�һ��
�����Ƶ��������ڵĿո�;����԰�һ����������
һ��(��һ��)������ͬɫ�����ӵ���ո�
����N = 3�����������״̬����Ϊ:
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

��Ӧ�Ŀո����ڵ�λ��(������)Ϊ:
3 5 6 4 2 1 3 5 7 6 4 2 3 5 4��


����һ������
�����ʽ
��������ո��������̵�λ�ã�ÿ���������ÿո�
�ָ���ÿ��5����(ÿ�н�β�޿ո����һ�п�
�Բ���5����;����ж����ƶ�������С�Ľ⣬��
����һ������С�Ľ�)

4

4 6 7 5 3
2 4 6 8 9
7 5 3 1 2
4 6 8 7 5
3 4 6 5
*/ 



























