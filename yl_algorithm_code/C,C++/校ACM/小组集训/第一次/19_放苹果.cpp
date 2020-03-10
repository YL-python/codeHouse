#include <iostream>
using namespace std;

int apple(int m,int n) {
	if(m == 0 || n == 1) {
		return 1;
	}
	if(n > m ) {
		return apple(m,m);
	}
	return apple(m-n, n) + apple(m, n-1);
}

int main() {
	int k;
	cin >> k;
	for(int i=0; i<k; i++) {
		int m,n;
		cin >> m>> n;
		cout << apple(m,n) << endl;
	}
}
/*
这个问题的关键是递推函数。

m个苹果放在n个盘子中，那么定义函数为apple(m,n)：

1.m=0，没有苹果，那么只有一种放法，即apple(0,n)=1

2.n=1，只有一个盘中，不论有或者无苹果，那么只有一种放法，apple(m,1)=1

3.n>m，和m个苹果放在m个盘子中是一样的，即apple(m,n)=apple(m,m)

4.m>=n，这时分为两种情况，一是所有盘子都有苹果，二是不是所有盘子都有苹果。
	不是所有盘子都有苹果和至少有一个盘子空着是一样的，即=apple(m,n-1)。
	所有盘子都有苹果，也就是至少每个盘子有一个苹果，m个苹果中的n个放在n个盘子中，
	剩下的m-n个苹果，这和m-n个苹果放在n个盘子中是是一样的，即=apple(m-n, n)。
	这时，apple(m,n)=apple(m-n, n)+apple(m,n-1)。
https://blog.csdn.net/weixin_38505045/article/details/88366785
*/

