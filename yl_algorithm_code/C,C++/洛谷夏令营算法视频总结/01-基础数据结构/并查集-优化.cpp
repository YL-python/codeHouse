/*
a->b->c->d->e...->n

并查集的复杂度在于查询的时候每一次都要 迭代去找根节点
a 找 b ,b 找 c, c。。。最后找到 n

现在把路径优化
a 找 b ,b 找 c, c。。。最后找到 n  之后
让 。。。 直接指向 n ... 让 c 指向 n ， 让 b 指向 n ， 让 a 指向 n
之后的查询时间复杂度就是 1
*/

#include <cstdio>

struct unionFind {
	int bin[100005];

	// 初始化  吧 i 染成 i 颜色
	unionFind() {
		for(int i=0; i<100005; i++)
			bin[i] = i;
	}

	// 查询 x 被染成什么颜色
	int find(int x) {
		if(bin[x] == x)
			return x;
		else {
			// 路径优化
//			bin[x] = find(bin[x]);
//			return bin[x];
			return bin[x] = find(bin[x]);
		}
//		return bin[x] == x ? x : (bin[x] = find(bin[x]));
	}

	// 合并操作 吧 x 染成 y 的颜色，也就是把两种颜色变成一种颜色
	// 修改所有颜色就只要修改最终根节点的颜色就行，因为查找颜色的时候是按照根节点颜色来的
	void uni(int x,int y) {
		bin[find(x)] = find(y);
	}

	void ask(int x,int y) {
		printf("%s\n",find(x) == find(y) ? "Yes" : "No");
	}
};

unionFind u;

int main() {
	int n,m,p,x,y;
	scanf("%d%d%d",&n,&m,&p);
	while(m --) {
		scanf("%d%d",&x,&y);
		u.uni(x,y);
	}
	while(p --) {
		scanf("%d%d",&x,&y);
		u.ask(x,y);
	}
	return 0;
}








