/*
���ֱض���ȷ��д��

r-l >5 ���������
ʣ��5�������Լ�ö��
*/
#include <cstdio>

int f(int n) {
	if(n>100)
		return 1;
	return 0;
}// ��һ����1���±���101  �ö����ҳ�

void search() {
	int l=1,r=1024,mid;
	while(r-l>5) {
		printf("[%d, %d]\n",l,r);
		mid = (l+r)/2;
		if(f(mid) == 0)
			l=mid+1;
		else
			r=mid;
	}
	for(; f(l)==0; l++);
	printf("%d\n",l);
}

int main() {
	search();
	return 0;
}
