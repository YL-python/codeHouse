#include <iostream>
using namespace std;

int a[25],n,k,ans=0;

int ss(int x) {
	for(int i=2; i*i<=x; i++) {
		if(x % i == 0) {
			return 0;
		}
	}
	return 1;
}

// �� cen �ϵ���  cet��ʾѡ���ǲ�ѡ  sum��ʾ��ǰ�ĺ�
void dfs(int cen,int cnt, int sum) {
	if(cen == n) {  // ����� n ����
		if(cnt == k) {  // ѡ������Ϊ k ����ʱ��
			if(ss(sum)) {
				ans++;
			}
		}
		return ;
	}
	dfs(cen+1,cnt,sum);  // ������һ�� ���ҵ�ǰ���ϵ�����ѡ
	dfs(cen+1,cnt+1,sum+a[cen]);  // ������һ�� ���ҵ�ǰ���ϵ���ѡ
}

int main() {
	cin >> n >> k;
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}
	dfs(0,0,0);
	cout << ans;
	return 0;
}
