#include <iostream>
#include <cmath>
using namespace std;

// ˼ά��Ҫ����ס�ˣ�ֻҪ������Ӿ��У���Ҫ���ǳ�������������������ʲô
// ��Ϊ������ҳ�����  %һ�� ʣ�µľ�������ķ���������

int main() {

	int n,maxlen=0,len,start=0;
	cin >> n;
	int sqrtn = sqrt(n);

	// �� �� i��ʼ������Ӿ���
	for(int i=2; i<=sqrtn; i++) {
		int temp = n;
		int j = i;
		len = 0;
//		while( ! temp % j)  ����д������ 
		while(temp % j == 0) {
			temp/=j;
			j++;
			len++;
		}
		if(len>maxlen) {
			start = i;
			maxlen = len;
		}
	}
	if(maxlen) {
		cout<<maxlen<<endl<<start;
		for(int i=start+1; i<maxlen+start; i++) {
			cout << "*" << i;
		}
	} else {
		cout << 1 << endl << n;
	}
	return 0;
}
