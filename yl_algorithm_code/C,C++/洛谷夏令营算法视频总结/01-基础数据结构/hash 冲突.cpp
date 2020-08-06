/*
hash ���������ʱ�临�Ӷȶ��� 1
����ȱ��������Ҫ���ĺܴ�

���ڽ���취�����������ȥ ģ һ���� �ж�ģ��������ڲ��������������
ȱ�㣬�������ײ  10007    5 �� 10012  ����ֵһ�����ǲ���ͬһ����

�����ͻ
+ ������ά��  Ҳ����������
+ ˫ģ��������ģ��
+ stl set ����

mod ��ȡֵһ����һ������   ��Ȼ�Ļ�  ż��ȥ ģ��ʱ�� ���������ȫ�� [0,mod]  ����Ŀռ��û����ȫ����
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

// ��ԭʼ
struct brute {
	bool w[1000005];
	void ins(int x) {
		w[x] = 1;
	}
	void ask(int x) {
		print("%d\n",w[x]);
	}
};

// ȡģ����
struct naive {
	bool w[mod + 5];
	void ins(int x) {
		w[x % mod] = 1;
	}
	void ask(int x) {
		print("%d\n",w[x]);
	}
};

// ������
struct zip {
	vector <int> w;
	void ins(int x) {
		// �� ģ ��ֵ��Ϊһ�����࣬��ֵ�ŵ������������
		w[x % mod].push_back(x);
	}
	void ask(int x) {
		bool flag = false;
		// ���������������û�����ֵ
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

	// set �������
	set <int> s; // �ײ��Ǻ���� �������ʱ�临�Ӷ��� logn  ֧�ֽṹ��
	unordered_set <int> us; // �ײ��� �������� hash �������ʱ�临�Ӷ��� 1   ��֧�ֽṹ��
	printf("%d\n",s.count(5))
	s.insert("5");
	printf("%d\n",s.count(5))
	return 0;
}
