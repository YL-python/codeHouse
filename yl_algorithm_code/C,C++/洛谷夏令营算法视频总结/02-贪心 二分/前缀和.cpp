/*
ǰ׺��
a���� ������� l,r���� �� l��r�ĺ�

sum[i]��ʾa����ǰ i���  ��a����� l-r ����� ������ sum[r+1] - sum[l]
*/

#include <cstdio>

int get_lr_sum(int l,int r) {
	return sum[r+1] - sum[l];
}

int main() {

	for(int i=0; i<n; i++) {
		scanf("%d",&a[i]);
		sum[i] += a[i];
	}

	return 0;
}
