#include <iostream>
using namespace std;

int main() {
	int b[105][105]= {0}; // i ��û�б� j�ἰ�� 
	int cnt[105]= {0};  // i���ἰ�Ĵ��� 
	int maxcnt=-1,hotpeople;
	int n,a,k,temp;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a >> k;
		for(int j=0; j<k; j++) {
			cin >> temp;  // a �ἰ�� temp
			b[temp][a] = 1;  // temp �� a �ἰ�� 
			cnt[temp]++;  //  temp �ἰ����++ 
		}
	}
	for(int i=0; i<105; i++) {
		if(cnt[i] > maxcnt) {
			maxcnt = cnt[i];
			hotpeople = i;
		}
	}
	cout << hotpeople << endl;
	for(int i=0; i<105; i++) {
		if(b[hotpeople][i]) {
			cout << i << " ";
		}
	}
	return 0;
}
