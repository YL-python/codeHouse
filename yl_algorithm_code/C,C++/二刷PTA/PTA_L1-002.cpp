#include<iostream>
using namespace std;
int main() {

	int n, m;
	char s;
	cin >> n >> s;
	// ����һ�������������ٸ�
	int cnt = 0;
	for(int i=1; i<1000; i+=2) {
		i==1 ? cnt += 1 : cnt += i*2;
		if(cnt > n) {
			m = i - 2;
			cnt -= i*2;
			break;
		}
	}
	// printf("%d  %d\n",m,cnt);
	// ���ʱ�� cnt �����˶��ٸ�  m��һ�������������ٸ�
	
	// ���
	for(int i=m; i>=0; i-=2) {
		for(int j=(m-i)/2; j>0; j--) {
			cout << " ";
		}
		for(int j=0; j<i; j++) {
			cout << s;
		}
		cout << endl;
	}
	
	for(int i = 3;i<=m;i+=2){
		for(int j=(m-i)/2; j>0; j--) {
			cout << " ";
		}
		for(int j=0; j<i; j++) {
			cout << s;
		}
		cout << endl;
	}
	cout << n-cnt;

	return 0;
}








