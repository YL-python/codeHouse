#include <iostream>
#include <algorithm>
using namespace std;

int a[] = {0,1,2,3,4,5,6,7,8,9};
int ans = 0;

bool xl(int x,int y) {
	int k = x>y?x-y:y-x;
	if(k == 1) {
		return true;
	} else {
		return false;
	}
}

bool test() {
	if(xl(a[0], a[1]) ||xl(a[0], a[3]) ||xl(a[0], a[4]) ||xl(a[0], a[5]) ||
	        xl(a[1], a[2]) ||xl(a[1], a[4]) ||xl(a[1], a[5]) ||xl(a[1], a[6]) ||
	        xl(a[2], a[5]) ||xl(a[2], a[6]) ||
	        xl(a[3], a[4]) ||xl(a[3], a[7]) ||xl(a[3], a[8]) ||
	        xl(a[4], a[5]) ||xl(a[4], a[7]) ||xl(a[4], a[8]) ||xl(a[4], a[9]) ||
	        xl(a[5], a[6]) ||xl(a[5], a[8]) ||xl(a[5], a[9]) ||
	        xl(a[6], a[9]) ||xl(a[7], a[8]) ||xl(a[8], a[9]) ) {
		return false;
	} else {
		return true;
	}
}

int main() {
	do {
		if(test()) {
			ans ++;
		}
	} while(next_permutation(a, a+10));
	cout << ans << endl;
	return 0;
}

/*

��������

���µ�10������
   +--+--+--+
   |0 |1 |2 |
+--+--+--+--+
|3 |4 |5 |6 |
+--+--+--+--+
|7 |8 |9 |
+--+--+--+

�������ʾ�����⣬Ҳ���Բο���ͼ1.jpg����

����0~9�����֡�Ҫ���������������ֲ������ڡ�
�����ҡ����¡��ԽǶ������ڣ�

һ���ж����ֿ��ܵ�����������

����д��ʾ������Ŀ��������
ע�⣺���ύ��Ӧ����һ����������Ҫ��д�κζ�������ݻ�˵�������֡�
*/
