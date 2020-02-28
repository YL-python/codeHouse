#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 10010;
int dp[maxn][2];  // 1 ��ʾ��ǰ����ϣ� 0 ��ʾû�� ��ǰ����� 
int w[maxn]; 
int f[35][35];

int main() {
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		cin >> w[i];
	} 
	dp[1][0] = 0;
	for(int i=2;i<=n;i++){
		// û������µ���߷��� ǰ����������ֵ 
		dp[i][0] = max(dp[i-1][0], dp[i-1][1]);
		// ��������µķ�����  
		dp[i][1] = dp[i-1][0] + w[i] * w[i-1];
	}
	cout << max(dp[n][0], dp[n][1]) << endl;
	return 0;
}
/*
��Ϸ�������������ѡ�������ɶ����ڵ����ӣ���
����ͬʱ��ȥ��ÿһ�����ӵ���ʧ������ʹ���ܷ�
����������������˵ķ�����ע�⣬ÿ������ֻ��
��- -�Σ�����������ȥ�Ժ󣬻���ռλ��

8
-9 -5 -4 -2 4 -5 -4 2 
*/ 
