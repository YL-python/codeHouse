/*
hash 表，插入查找时间复杂度都是 1
但是缺点是数组要开的很大

现在解决办法就是让这个数去 模 一个属 判断模的这个数在不在这个数组里面
缺点，会产生碰撞  10007    5 和 10012  返回值一样但是不是同一个数

解决冲突
+ 用链表维护  也叫做拉链法
+ 双模法或者三模法
+ stl set 方法

mod 的取值一般是一个质数   不然的话  偶数去 模的时候 结果不会完全是 [0,mod]  数组的空间就没有完全利用
233
2333
23333
19260817
10009
2147483647 
*/
#include <cstdio>
#include <vector>
#include <set>
#define mod 10007;

using namespace std;

// 最原始
struct brute {
	bool w[1000005];
	void ins(int x) {
		w[x] = 1;
	}
	void ask(int x) {
		print("%d\n",w[x]);
	}
};

// 取模方法
struct naive {
	bool w[mod + 5];
	void ins(int x) {
		w[x % mod] = 1;
	}
	void ask(int x) {
		print("%d\n",w[x]);
	}
};

// 拉链法
struct zip {
	vector <int> w;
	void ins(int x) {
		// 把 模 的值作为一个分类，把值放到这个分类里面
		w[x % mod].push_back(x);
	}
	void ask(int x) {
		bool flag = false;
		// 看这个分类年面有没有这个值
		for(auto i=w[x % mod].begin(); i!=w[x % mod].end(); i++) {
			if(*i == x) {
				flag = true;
			}
		}
		if(flag) {
			puts("Yes");
		} else {
			puts("No");
		}
	}
};


brute b;

int main() {
	b.ask(5);
	b.ins(5);
	b.ask(5);
	b.ins(6);
	b.ask(6);

	// set 方法解决
	set <int> s; // 底层是红黑树 插入查找时间复杂度是 logn  支持结构体
	unordered_set <int> us; // 底层是 拉链法的 hash 插入查找时间复杂度是 1   不支持结构体
	printf("%d\n",s.count(5))
	s.insert("5");
	printf("%d\n",s.count(5))
	return 0;
}
