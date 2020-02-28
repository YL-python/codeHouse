#include <iostream>
#include <string>
#include <queue>

using namespace std;



int main(){
	
	queue<int> q;
	q.push(1);
	q.push(2);	
	q.push(3);
	
	cout << q.size() << endl;
	
	while(! q.empty()){
		cout << q.front() << endl;
		q.pop();
	}
	
	// 没有清空方法 只能手动清空  while 循环加 pop  
	
	return 0;
}




























