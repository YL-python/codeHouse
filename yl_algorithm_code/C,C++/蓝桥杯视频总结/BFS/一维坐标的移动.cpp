#include <iostream>
#include <string>
#include <queue>
using namespace std;
int n,A,B;
bool vis[5010];
queue<pair<int, int> > q;  // 空格一定要打 

bool in(int x){
	return x>=0 && x<n;
} 

int main(){
	
	cin >> n >> A >> B;
	q.push(make_pair(A, 0));  // 当前点和步数 
	vis[A] = true;
	
	int now=A,step=0;  // 队列性质，第一个访问到的值就是最小值 
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



























