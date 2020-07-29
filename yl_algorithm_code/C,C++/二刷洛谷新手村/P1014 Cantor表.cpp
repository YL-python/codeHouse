#include <iostream>
using namespace std;

int N,n,m;

int main() {
	cin >> N;
	// 求N在哪一层上,和这一层最大值的ca
	int temp=0,chen = 0,ca = 0;
	for(int i=1; i<=1000000; i++) {
		temp += i;
		if(temp >= N) {
			chen = i;
			ca = temp - N;
			break;
		}
	}
//	cout << chen << " " << ca << endl;
	// chen  层数有了，就要判断是上升层还是下降层
	if(chen % 2) {  // 上升层
		cout << 1+ca << "/" << chen-ca;
	} else {  // 下降层
		cout << chen-ca << "/" << 1+ca;
	}
	return 0;
}
