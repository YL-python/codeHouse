#include <stdio.h>
#define N 6
#define M 5
#define BUF 1024

// k ���� 0		m ���� M	b ����� 
void f(int a[], int k, int m, char b[])
{
	int i,j;
	
	if(k==N){ 
		b[M] = 0;
		if(m==0) printf("%s\n",b);
		return;
	}
	
	for(i=0; i<=a[k]; i++){  // ������ 
		for(j=0; j<i; j++) b[M-m+j] = k+'A';  // �����ɳ���������ַ���
		// �ݹ��ɳ� 
		f(a,k+1,m-i,b);  // ��һ���ɳ������� ��Ҫ��������ȥ�Ѿ��ɳ������� 
	}
}
int main()
{	
	int  a[N] = {4,2,2,1,1,3};
	char b[BUF];
	f(a,0,M,b);
	return 0;
}

/*

��ǩ

X����Ҫ�ɳ�һ��5����ɵĹ۲���ǰ��W�ǡ�
���У�
A���������ɳ�4�ˡ�
B���������ɳ�2�ˡ�
C���������ɳ�2�ˡ�
....

��ô��������W�ǵĹ۲��Ż��ж����ֹ���Ĳ�ͬ����أ�

����ĳ�������������⡣
����a[] �м���ÿ�����ҿ����ɳ����������
����ִ�н��Ϊ��
DEFFF
CEFFF
CDFFF
CDEFF
CCFFF
CCEFF
CCDFF
CCDEF
BEFFF
BDFFF
BDEFF
BCFFF
BCEFF
BCDFF
BCDEF
....
(����ʡ�ԣ��ܹ�101��)


#include <stdio.h>
#define N 6
#define M 5
#define BUF 1024

void f(int a[], int k, int m, char b[])
{
	int i,j;
	
	if(k==N){ 
		b[M] = 0;
		if(m==0) printf("%s\n",b);
		return;
	}
	
	for(i=0; i<=a[k]; i++){
		for(j=0; j<i; j++) b[M-m+j] = k+'A';
		______________________;  //���λ��
	}
}
int main()
{	
	int  a[N] = {4,2,2,1,1,3};
	char b[BUF];
	f(a,0,M,b);
	return 0;
}

��ϸ�Ķ����룬��д���߲���ȱ�ٵ����ݡ�

ע�⣺��Ҫ��д�κ��������ݻ�˵�������֡�

*/
