#include <iostream>
using namespace std;

int main() {
	int a=9,b,c,d;
	int n=1,m=0,x;
	// c=b+1 , c+x>10
	/*
	      9 b c d
	  +   1 0 x b
	-------------------
	   	1 0 c b e
	*/
	for(b=2; b<=7; b++) {
		for(x=2; x<=8; x++) {
			for(d=2; d<=8; d++) {
				c = b+1;
				if(b == x || b==d || x == c || x == d || d == c) {
					continue;
				}
				int jian = (9000+b*100+c*10+d) + (1000+x*10+b) - (10000+c*100+b*10);
				if(jian >= 2 && jian < 8 ) {
					if(jian != b && jian != c && jian != d && jian != x  && jian != 1 && jian != 0 && jian != 9) {
						printf(" 9%d%d%d\n 10%d%d\n10%d%d%d\n----------\n",b,c,d,x,b,c,b,jian);
					}
				}

			}
		}
	}
	cout << "wanchenle" << endl;
	return 0;
}

/*

��������

�۲�����ļӷ���ʽ��

      �� �� �� ��
  +   �� �� �� ��
-------------------
   �� �� �� �� ��

(����ж������⣬���Բο���ͼ1.jpg��)

���У���ͬ�ĺ��ִ�����ͬ�����֣���ͬ�ĺ��ִ���ͬ�����֡�

������д�����������������4λ���֣���Ψһ������Ҫ��д�κζ������ݡ�

      a b c d
  +   n m x b
-------------------
   	n m c b e

����һЩ����
a + n ��λ����n ==> n=1 , a=9 �� 8
a + n ��λ֮����m ==> m=0 ==> a=9

      9 b c d
  +   1 0 x b
-------------------
   	1 0 c b e

b + 0 = c ��b,c����һ���� == > c=b+1 , c+x>10

*/

