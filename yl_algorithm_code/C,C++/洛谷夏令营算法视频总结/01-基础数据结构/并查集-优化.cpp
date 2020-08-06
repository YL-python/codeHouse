/*
a->b->c->d->e...->n

���鼯�ĸ��Ӷ����ڲ�ѯ��ʱ��ÿһ�ζ�Ҫ ����ȥ�Ҹ��ڵ�
a �� b ,b �� c, c����������ҵ� n

���ڰ�·���Ż�
a �� b ,b �� c, c����������ҵ� n  ֮��
�� ������ ֱ��ָ�� n ... �� c ָ�� n �� �� b ָ�� n �� �� a ָ�� n
֮��Ĳ�ѯʱ�临�ӶȾ��� 1
*/

#include <cstdio>

struct unionFind {
	int bin[100005];

	// ��ʼ��  �� i Ⱦ�� i ��ɫ
	unionFind() {
		for(int i=0; i<100005; i++)
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
//		return bin[x] == x ? x : (bin[x] = find(bin[x]));
	}

	// �ϲ����� �� x Ⱦ�� y ����ɫ��Ҳ���ǰ�������ɫ���һ����ɫ
	// �޸�������ɫ��ֻҪ�޸����ո��ڵ����ɫ���У���Ϊ������ɫ��ʱ���ǰ��ո��ڵ���ɫ����
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








