/*
a���� �� l,r��Χ��ÿһ�μ���k
���ִ��   Ҫ��ʱ�临�Ӷ��� On

֪��ÿһ��Ԫ�ر�ǰ��Ԫ�ض༸�����Ƴ��������

l �� r �������k����
a[l] ��ʼ��ǰ��һ��Ԫ�ض� k , a[r+1] ��ʼ��ǰ��ÿ��Ԫ���� k

��һ�������ʾ ÿһ��Ԫ�غ�ǰһ��Ԫ�صĲ�
p[i] = a[i] - a[i-1]

l �� r �������k�ͱ����
p[l]+=k
p[r+1]-=k
*/
#include <cstdio>

int a[100],p[100];

void add(int l,int r,int k) {
	p[l]+=k;
	p[r+1]-=k;
}

void get_a() {
	for(int i=1; i<=n; i++) {
		a[i] = a[i-1]+p[i];
	}
}

int main() {

	return 0;
}
