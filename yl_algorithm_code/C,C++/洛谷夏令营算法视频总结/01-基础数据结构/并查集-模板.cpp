/*
https://www.luogu.com.cn/problem/P3367
不优化会有三个测试点过不去
*/

#include <cstdio>

struct unionFind {
	int bin[100005];

	// 初始化  吧 i 染成 i 颜色
	unionFind() {
		for(int i=0; i<10005; i++)
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
	}

	// 合并操作 吧 x 染成 y 的颜色，也就是把两种颜色变成一种颜色
	// 修改所有颜色就只要修改最终根节点的颜色就行，因为查找颜色的时候是按照根节点颜色来的
	void uni(int x,int y) {
		bin[find(x)] = find(y);
	}

	void ask(int x,int y) {
		printf("%s\n",find(x) == find(y) ? "Y" : "N");
	}
};

unionFind u;

int main() {
	int n,m,z,x,y;
	scanf("%d%d",&n,&m);
	while(m --) {
		scanf("%d%d%d",&z,&x,&y);
		if(z == 1) {
			u.uni(x,y);
		} else {
			u.ask(x,y);
		}
	}
	return 0;
}








