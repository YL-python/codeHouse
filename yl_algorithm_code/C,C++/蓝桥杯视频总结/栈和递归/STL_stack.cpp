#include <iostream>
#include <string>
#include <stack>
using namespace std;



int main(){

	stack<string> s;
	
	s.push("s111");
	s.push("s222");
	s.push("s333");
	s.push("s444");
	
	cout << s.size() << endl;
	
	while(!s.empty()){
		cout << s.top() << endl;
		s.pop();
	}
	
	cout << s.size() << endl;
	
	return 0;
}




























