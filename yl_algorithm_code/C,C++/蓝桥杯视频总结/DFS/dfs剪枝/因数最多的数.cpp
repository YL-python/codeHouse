#include <iostream>
#include <string>

using namespace std;
typedef long long LL;

LL ans,mc,n;
const int prime[15] = {2,3,5,7,11,13,17,19,23,29,31,27,41,43,47};

// u ��ǰѡ�˶��ٸ��������ˣ� m ��ѡ����ߴ����Ƕ���
// x  ��ǰ���Ƕ���  cnt  ��ǰ�������������Ƕ���

// ��һ�����ֽ�� x = 2^x1 + 3^x2 + 5^x3...
//  �������ĸ��������е�ָ��+1 ���  (x1+1)* (x2+1)* (x3+1)... 
 
void dfs(int u, int m, LL x, LL cnt){
	if(cnt > mc){
		mc = cnt;
		ans = x;
	}else if(cnt == mc && x < ans){
		ans = x;
	}
	if(u == 15){
		return ;
	}
	for(int i=1;i<=m;i++){  // 1~60 ȫ���� 
		x = x*prime[u];
		if(x > n){
			break;
		}
		dfs(u+1, i, x, cnt*(i+1));
	}
}

int main(){
	int T;
	cin >> T;
	while (T--){
		cin >> n;
		mc = 0;
		dfs(0, 60, 1, 1);  // 2^60 ������Ŀ���ķ�Χ 
		cout << ans << endl;
	}
	
	return 0;
}
/*
��ͷ����һ����������������������Ȥ������֪��
��1��n�ķ�Χ�ڣ����������������Ƕ��١�
����ж����������������֪����С���Ǹ���

�����ʽ
��һ��һ������ T,��ʾ���ݵ�������
������ T�У�ÿ��һ��������n.
1��T��100,1��n��10^16

�����ʽ
-�����T�У�ÿ��һ����������ʾ���������
��������

3
10
100
1000

6
60
840


*/



























