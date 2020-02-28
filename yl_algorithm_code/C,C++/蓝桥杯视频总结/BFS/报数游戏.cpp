#include <iostream>
#include <string>
#include<queue>

using namespace std;



int main(){
	int n,m;
	queue<int> q;
	 
	// n 个人围成一圈，报数报到 m 的离开 
	cin >> n >> m;
	for(int i=1;i<=n;i++){
		q.push(i);
	}
	int cnt=1;
	while(q.size() > 1){
		int temp = q.front();
		q.pop();
		if(cnt == m){
			cnt = 1;
		}else{
			q.push(temp);
			cnt++;
		}
	}
	cout << q.front() << endl;
	
	return 0;
}




























