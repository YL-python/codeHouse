#include <iostream>
using namespace std;

// �ⷨ1  ֱ�� �ݹ� �¼����Ӷ��� n��n�η�  25 ��

int n,ans = 1;
int vis[1005];

void fun(int x) {
	if(x/2 == 0) {
		return;
	}
	for(int i=1; i<=x/2; i++) {
		fun(i);
	}
}

int main() {
	cin >> n;
	fun(n);
	cout << ans;
	return 0;
}
