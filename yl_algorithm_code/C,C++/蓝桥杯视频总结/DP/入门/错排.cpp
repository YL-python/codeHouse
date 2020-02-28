#include <iostream>
using namespace std;
typedef long long ll;
const int N = 1e3 + 9;
int f[N];
int main() {
	int n;
	cin >> n;
	f[1] = 0;
	f[2] = 1;
	for(int i=3; i<=n; i++) {
		f[i] = (f[i-1] + f[i-2]) * (i - 1);
	}
	cout << f[n] << endl;
	return 0;
}
/*
	���Ź�ʽ��
	fn = (n - 1) * ( fn-1 + fn-2)
	
	n ������ ������ F(n)�����ƿ���
	n-1 ������֮��,�õ�n���� ȥ����  ����F(n-1) * n-1
	����������� n-1������һ���ǶԵ� n-2���д��ţ�Ȼ�� ��n����ȥ������ԵĽ���
	���� F(n-2) * n-1
	�;���  fn = (n - 1) * ( fn-1 + fn-2)
	
	���Ǳ߽磬 F1 = 0��F2 = 1 
*/
