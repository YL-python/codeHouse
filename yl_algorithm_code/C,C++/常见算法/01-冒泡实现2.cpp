/*
ð�������������ʵ��
*/

# include <stdio.h>
int main(void) {
	int a[] = {900, 2, 3, -58, 34, 76, 32, 43, 56, -70, 35, -234, 532, 543, 2500};
	int n;  //�������a��Ԫ�صĸ���
	int i;  //�Ƚϵ�����
	int j;  //ÿ�ֱȽϵĴ���
	int buf;  //��������ʱ���ڴ���м�����
	n = sizeof(a) / sizeof(a[0]);  /*a[0]��int��, ռ4�ֽ�, �����ܵ��ֽ�������4����Ԫ�صĸ���*/

	for(i = 0; i < n - 1; i++) {
		for(j = n - 1; j > i; j--) {
			if (a[j] < a[j - 1]) {
				buf = a[j - 1];
				a[j -1] = a[j];
				a[j] = buf;
			}
		}
	}

	for (i=0; i<n; ++i) {
		printf("%d\x20", a[i]);
	}
	printf("\n");
	return 0;
}
