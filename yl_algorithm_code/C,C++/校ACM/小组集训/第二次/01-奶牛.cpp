#include <iostream>
using namespace std;

// ���ݷ�Χ�� 10����η���ֱ������for ����ö�ٲ��ᳬʱ
// �����Ǳ�׼�� dp ��������

int main() {
	int n;
	int a[100005];
	int dp;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	dp = a[0];
	int ans = a[0];
	for(int i=1; i<n; i++) {
		dp = max(dp+a[i],a[i]);
		if(dp > ans){
			ans = dp;
		}
	}
	cout << ans;
	return 0;
}
