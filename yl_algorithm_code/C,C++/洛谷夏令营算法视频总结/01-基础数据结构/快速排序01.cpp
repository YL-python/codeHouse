#include <cstdio>

int a[1000005],n;

void qsort(int l,int r) { //Ӧ�ö���˼��
	int mid=a[(l+r)/2];//�м���
	int i=l,j=r;
	do {
		while(a[i]<mid) i++;//������벿�ֱ��м��������
		while(a[j]>mid) j--;//�����Ұ벿�ֱ��м���С����
		if(i<=j) { //�����һ�鲻����������������С�Ҵ󣩵���
			int t=a[i];
			a[i] = a[j];
			a[j] = t;
			// ���� ++  --  �������
			i++;
			j--;
		}
	} while(i<=j);//����ע��Ҫ��=
	if(l<j) qsort(l,j);//�ݹ�������벿��
	if(i<r) qsort(i,r);//�ݹ������Ұ벿��
}

int main() {
	scanf("%d",&n);
	for(int i=1; i<=n; i++) {
		scanf("%d",&a[i]);
	}
	qsort(1,n);
	for(int i=1; i<=n; i++) {
		printf("%d ",a[i]);
	}
	return 0;
}
