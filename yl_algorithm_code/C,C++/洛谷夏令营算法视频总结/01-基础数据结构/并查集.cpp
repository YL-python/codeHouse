/*
亲戚问题 a-b是亲戚 a-c是亲戚。。。构成一个亲戚树
判断 两个人是不是亲戚关系就看他们有没有共同的 根亲戚
a-b a-c 每次输入的a可以有很多节点 但是 b,c的指向就是唯一的
所以每一次输入吧 后面的指向前面的（染成前面的颜色）
最后查询两个人  是否有相同颜色的

时间复杂度 最坏是 N平方

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
		else
			return find(bin[x]);
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








