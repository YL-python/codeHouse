/*
https://www.luogu.com.cn/problem/P3367
���Ż������������Ե����ȥ
*/

#include <cstdio>

struct unionFind {
	int bin[100005];

	// ��ʼ��  �� i Ⱦ�� i ��ɫ
	unionFind() {
		for(int i=0; i<10005; i++)
			bin[i] = i;
	}

	// ��ѯ x ��Ⱦ��ʲô��ɫ
	int find(int x) {
		if(bin[x] == x)
			return x;
		else {
			// ·���Ż�
//			bin[x] = find(bin[x]);
//			return bin[x];
			return bin[x] = find(bin[x]);
		}
	}

	// �ϲ����� �� x Ⱦ�� y ����ɫ��Ҳ���ǰ�������ɫ���һ����ɫ
	// �޸�������ɫ��ֻҪ�޸����ո��ڵ����ɫ���У���Ϊ������ɫ��ʱ���ǰ��ո��ڵ���ɫ����
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








