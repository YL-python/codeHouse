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
	
	// û����շ��� ֻ���ֶ����  while ѭ���� pop  
	
	return 0;
}




























