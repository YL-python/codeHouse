#include <cstdio>
#include <stack>
using namespace std;

int main() {
	stack <char> s;
	char a[1005];
	scanf("%s",a);

	bool flag = true;
	for(int i=0; a[i]; i++) {
		if(a[i] == '(' || a[i] == '{' || a[i] == '[')
			s.push(a[i]);
		else {
			if(s.empty()) {
				flag = false;
				break;
			}
			if( (s.top() == '(' && a[i] == ')') ||
			        (s.top() == '[' && a[i] == ']') ||
			        (s.top() == '{' && a[i] == '}')
			  ) {
				s.pop();
			} else {
				flag = false;
				break;
			}
		}
	}
	if(!s.empty()) flag = false;
//	if(s.size()) flag = false;

	if(flag) {
		puts("YES!!!");
	} else {
		puts("N0!!!");
	}
	return 0;
}
