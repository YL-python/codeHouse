#include <iostream>
#include <map>
using namespace std;

int n,k,a[100005],s[100005];
map<int,int> cnt; // ͬ������ͳ��

int main() {
	cin >> n >> k;
	s[0] = 0;
	cnt[0] = 1;
	for(int i=1; i<=n; i++) {
		cin >> a[i];
		s[i] = (s[i-1] + a[i]) % k;  // ǰ׺�͵�ͬ������ 
		cnt[s[i]] ++;
	}
	long long ans = 0;
//	for(int i=1; i<=n; i++) {
//		for(int j=i; j<=n; j++) {
//			if(s[j] - s[i-1] % k == 0) {
//				ans++;
//			}
//		}
//	}
	for(int i=0; i<k; i++) {  // ������Ȼ�� 0~k-1֮��
		ans += (long long) cnt[i] * (cnt[i] - 1) / 2;
	}
	cout << ans << endl;
	return 0;
}
