#include <iostream>
#include <climits>
#include <cmath>
using namespace std;

const int N = 1000;
// f1 f2 f3 表示1 2 3部手机时第1成的最坏测试数
int f1[N+1],f2[N+1],f3[N+1];

int main() {
	// 只有一部手机的情况下，最坏测试情况只能是从第一层开始一个一个往上测试
	// 所以最坏的情况就是 i
	for(int i=1; i<=N; i++) {
		f1[i] = i;
	}

	// 两部手机的情况
	for(int i=1; i<=N; i++) {
		int ans = INT_MAX;
		for(int j=1; j<=i; j++) {
			// min 是最优策略  max是最坏情况
			// 在j层测试 摔坏就是 还要测试 f1[i-j]  没摔快就是 f2[j-1]
			ans = min(ans,1+max(f1[i-j],f2[j-1]));
		}
		f2[i] = ans;
	}
	// 三部手机的情况
	for(int i=1; i<=N; i++) {
		int ans = INT_MAX;
		for(int j=1; j<=i; j++) {
			ans = min(ans,1+max(f2[i-j],f3[j-1]));
		}
		f3[i] = ans;
	}
	printf("%d",f3[1000]);
	return 0;
}
