#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

int main() {

	int n;
	cin >> n;

	vector<int > a(n);

	// 存给定的 a 序列
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}

	stack<int > s;
	int cur = 1;  // 记录位置变量
	int f = 1;   // 是否可以按 a 顺序出栈

	// 一个栈 先是空  
	for(int i=0; i<n; i++) {
		// 看栈顶是不是 a[i] 不是就吧 cur 进栈 
		// while 循环找到栈顶是a[i]的时候就停止进站，并且控制最多进 n 个火车 
		while((s.empty() || s.top() != a[i]) && cur<=n){
			s.push(cur);
			cur++;  // 按 1~n 的顺序进站 
		}
		// 进站操作完成之后 如果栈顶不是 a[i] 或者是空栈表示不能按 a 顺序出站 
		if (s.empty() || s.top()!=a[i]){
			f = 0;
			break;
		}else{
			s.pop();
		}
	}

	if(f){
		cout << "可以    按 a 顺序出站" << endl;
	}else{
		cout << "不可以    按 a 顺序出站" << endl;
	}

	return 0;
}
/*
给 n 个数，入栈顺序是 1，2，3...n
再给一个排列 a
判断出栈顺序是否可以是 a
*/



























