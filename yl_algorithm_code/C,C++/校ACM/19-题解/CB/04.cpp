#include <iostream>
using namespace std;

// 暴力蓝桥，直接暴力
// 细节就是 怎么去重

// 包含2 和 4 的数字对应的 vis数组的值是0
int vis[2500];

bool have2or4(int x) {
	while(x) {
		if(x%10 == 2 || x%10 == 4) {
			return true;
		}
		x/=10;
	}
	return false;
}

void init() {
	for(int i=0; i<=2500; i++) {
		if(have2or4(i)) {
			vis[i] = 1;
		}
	}
}


main() {
	int ans = 0; 
	init();
	for(int i=1; i<=2019; i++) {
		// j = i+1 去重 
		for(int j=i+1; j<=2019; j++) {
			for(int k=j+1; k<=2019; k++) {
				if(!vis[i] && !vis[j] && !vis[k] && i+j+k==2019){
					ans++;
				}
			}
		}
	}
	cout << ans;
	return 0;
}
/*
 把 2019 分解成 3 个各不相同的正整数之和，并且要求每个正整数都不包
 含数字 2 和 4，一共有多少种不同的分解方法？
 注意交换 3 个整数的顺序被视为同一种方法，例如 1000+1001+18 和
 1001+1000+18 被视为同一种。
*/
