#include <iostream>
#include <string>
#include <queue>
using namespace std;
int n,A,B;
bool vis[5010];
queue<pair<int, int> > q;  // �ո�һ��Ҫ�� 

bool in(int x){
	return x>=0 && x<n;
} 

int main(){
	
	cin >> n >> A >> B;
	q.push(make_pair(A, 0));  // ��ǰ��Ͳ��� 
	vis[A] = true;
	
	int now=A,step=0;  // �������ʣ���һ�����ʵ���ֵ������Сֵ 
	while(! q.empty()){
		now = q.front().first;
		step = q.front().second;
		q.pop();
		if(now == B){
			cout << step << endl;
			break;
		}
		int next = now+1;
		if(in(next) && vis[next] != true){
			q.push(make_pair(next,step+1));
			vis[next] = true;
		}
		next = now-1;
		if(in(next) && vis[next] != true){
			q.push(make_pair(next,step+1));
			vis[next] = true;
		}
		next = now * 2;
		if(in(next) && vis[next] != true){
			q.push(make_pair(next,step+1));
			vis[next] = true;
		}
	}
	
	return 0;
}
/*
10 2 7

3
*/ 



























