#include <iostream>
#include <algorithm>
using namespace std;

// ���ݷ�Χ100 ûɶ��˵��  ����
int n,cnt;
int a[105];
int vis[10005];  // ��¼��Щ�����ֹ� 

int main() {
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> a[i];
		vis[a[i]] = 1; // ��������ֹ� 
	}
	int ans = 0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<i; j++) {
			// vis ����Խ������ 
			if(a[i] + a[j] <= 10000 &&  vis[a[i] + a[j]]) { // ��������ֹ�
				ans ++;
				// �ù������Ͳ����ڼ��� ��Ȼ�𰸾Ͷ��ˡ� 
				vis[a[i] + a[j]] = 0;
			}
		}
	}
	cout << ans;
	return 0;
}
