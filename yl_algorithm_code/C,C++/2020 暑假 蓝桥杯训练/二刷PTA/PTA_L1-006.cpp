#include <iostream>
#include <cmath>
using namespace std;

// 思维不要被困住了，只要求最长因子就行，不要考虑除了最长的以外的数可以是什么
// 因为最长因子找出来了  %一下 剩下的就是另外的非连续因子

int main() {

	int n,maxlen=0,len,start=0;
	cin >> n;
	int sqrtn = sqrt(n);

	// 找 从 i开始的最长因子就行
	for(int i=2; i<=sqrtn; i++) {
		int temp = n;
		int j = i;
		len = 0;
//		while( ! temp % j)  这样写有问题 
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
