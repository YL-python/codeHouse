#include <iostream>
#include <string>

using namespace std;
typedef long long LL;

LL ans,mc,n;
const int prime[15] = {2,3,5,7,11,13,17,19,23,29,31,27,41,43,47};

// u 当前选了多少个质因子了， m 可选的最高次项是多少
// x  当前数是多少  cnt  当前数的质因子数是多少

// 把一个数分解成 x = 2^x1 + 3^x2 + 5^x3...
//  则因数的个数是所有的指数+1 相乘  (x1+1)* (x2+1)* (x3+1)... 
 
void dfs(int u, int m, LL x, LL cnt){
	if(cnt > mc){
		mc = cnt;
		ans = x;
	}else if(cnt == mc && x < ans){
		ans = x;
	}
	if(u == 15){
		return ;
	}
	for(int i=1;i<=m;i++){  // 1~60 全排列 
		x = x*prime[u];
		if(x > n){
			break;
		}
		dfs(u+1, i, x, cnt*(i+1));
	}
}

int main(){
	int T;
	cin >> T;
	while (T--){
		cin >> n;
		mc = 0;
		dfs(0, 60, 1, 1);  // 2^60 大于题目给的范围 
		cout << ans << endl;
	}
	
	return 0;
}
/*
蒜头君对一个数的因数个数产生了兴趣，他想知道
在1到n的范围内，因数个数最多的数是多少。
如果有多个这样的数，他想知道最小的那个。

输入格式
第一行一个整数 T,表示数据的组数。
接下来 T行，每行一个正整数n.
1≤T≤100,1≤n≤10^16

输出格式
-共输出T行，每行一个正整数表示最多因数个
数的数。

3
10
100
1000

6
60
840


*/



























