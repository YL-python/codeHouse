#include <stdio.h>
#define N 6
#define M 5
#define BUF 1024

// k 国家 0		m 人数 M	b 情况表 
void f(int a[], int k, int m, char b[])
{
	int i,j;
	
	if(k==N){ 
		b[M] = 0;
		if(m==0) printf("%s\n",b);
		return;
	}
	
	for(i=0; i<=a[k]; i++){  // 派人数 
		for(j=0; j<i; j++) b[M-m+j] = k+'A';  // 根据派出的人填充字符串
		// 递归派出 
		f(a,k+1,m-i,b);  // 下一次派出的人是 需要的人数减去已经派出的人数 
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

抽签

X星球要派出一个5人组成的观察团前往W星。
其中：
A国最多可以派出4人。
B国最多可以派出2人。
C国最多可以派出2人。
....

那么最终派往W星的观察团会有多少种国别的不同组合呢？

下面的程序解决了这个问题。
数组a[] 中既是每个国家可以派出的最多的名额。
程序执行结果为：
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
(以下省略，总共101行)


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
		______________________;  //填空位置
	}
}
int main()
{	
	int  a[N] = {4,2,2,1,1,3};
	char b[BUF];
	f(a,0,M,b);
	return 0;
}

仔细阅读代码，填写划线部分缺少的内容。

注意：不要填写任何已有内容或说明性文字。

*/
