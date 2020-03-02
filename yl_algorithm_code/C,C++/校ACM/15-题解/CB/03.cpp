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

三羊献瑞

观察下面的加法算式：

      祥 瑞 生 辉
  +   三 羊 献 瑞
-------------------
   三 羊 生 瑞 气

(如果有对齐问题，可以参看【图1.jpg】)

其中，相同的汉字代表相同的数字，不同的汉字代表不同的数字。

请你填写“三羊献瑞”所代表的4位数字（答案唯一），不要填写任何多余内容。

      a b c d
  +   n m x b
-------------------
   	n m c b e

先推一些数字
a + n 进位还是n ==> n=1 , a=9 或 8
a + n 进位之后余m ==> m=0 ==> a=9

      9 b c d
  +   1 0 x b
-------------------
   	1 0 c b e

b + 0 = c 又b,c不是一个数 == > c=b+1 , c+x>10

*/

