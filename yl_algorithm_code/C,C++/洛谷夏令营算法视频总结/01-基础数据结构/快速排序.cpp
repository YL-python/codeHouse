#include <cstdio>

int a[1000005],n;

void qsort(int l,int r) {
	int i=l, j=r, mid=a[(l+r)/2];
	while(i<=j) {  // ��������ָ��ͬһ����
		while(a[i]<mid) {
			// a[i] �� mid С��ʱ��ͻ�һֱ��  ֱ�����ֵ���ڵ��� mid �ͻ�ͣ��
			i++;
		}
		while(a[j]>mid) {
			// a[j] ���� mid ��ʱ��ͻ�һֱ��  ֱ�����ֵС�ڵ���  mid �ͻ�ͣ��
			j--;
		}
		// ���ʱ�� i �Ǵ��ڵ��� mid ���±�  j ��С�ڵ��� mid ���±�
		if(i<=j) {
			int t=a[i];
			a[i] = a[j];
			a[j] = t;
			// ����ǿ�Ƶ� ++ -- ���ܱ��������ָ��ͬһ�������������
			i++;
			j--;
		}
	}
	// ���ʱ�� ��������� [] mid []  ���ȫ��С��mid���� �� �ұ�ȫ�Ǵ��ڵ���mid ��
	// i ��ָ���һ������ mid ���±�+1  j ����ָ���������С�� mid ���±�-1

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
