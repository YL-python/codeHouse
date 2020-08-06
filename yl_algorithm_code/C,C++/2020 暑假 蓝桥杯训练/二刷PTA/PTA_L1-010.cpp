#include<iostream>
using namespace std;

int main() {
	int a,b,c,t;
	cin >> a >> b >> c;
	// ab
	a>b?t=a,a=b,b=t:1;
	// ac
	a>c?t=a,a=c,c=t:1;
	// bc
	b>c?t=b,b=c,c=t:1;
	
	cout << a<< "->" << b << "->" <<c;
	return 0;
}
