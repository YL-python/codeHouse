#include <set>
#include <iostream>
using namespace std;
int a[] = {0,0,0,0,0,0,0,1,1,1,1,1},ans;
set<string> s1;

void dfs(int g[3][4],int i,int j) {
	g[i][j] = 0;
	if(i-1 >= 0 && g[i-1][j] == 1) dfs(g,i-1,j);
	if(i+1 <= 2 && g[i+1][j] == 1) dfs(g,i+1,j);
	if(j-1 >= 0 && g[i][j-1] == 1) dfs(g,i,j-1);
	if(j+1 <= 3 && g[i][j+1] == 1) dfs(g,i,j+1);
}

bool check() {
	int g[3][4];
	// һάת��ά
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			if(a[i*4+j] == 1) g[i][j] = 1;
			else g[i][j] = 0;
		}
	}
	// �� g ����ͨ�Լ��
	int cnt = 0;  // ��ͨ��ĸ���
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			if(g[i][j] == 1) {
				dfs(g,i,j);
				cnt++;
			}
		}
	}
	return cnt == 1;
}

bool isExist() {
	string a_str;
	for(int i=0; i<12; i++) {
		a_str.insert(a_str.end(),a[i] + '0');
	}
	if(s1.find(a_str) != s1.end()) {
		return true;
	} else {
		s1.insert(a_str);
		return false;
	}
}

void f(int k) {
	if(k == 12) {
		if(!isExist() && check()) {
			ans++;
		}
	}
	for(int i=k; i<12; i++) {
		{
			int t=a[i];
			a[i]=a[k];
			a[k]=t;
		}
		f(k+1);
		{
			int t=a[i];
			a[i]=a[k];
			a[k]=t;
		}
	}
}
// ��ȥ�� 90 �����
// ȥ�� 90 * 12 �����  ʱ����ڰ��������ַ�����ѭ��
int main() {
	f(0);
	cout << ans << endl;
	return 0;
}
/*
{ int t=a[i]; a[i]=a[k]; a[k]=t; }
*/
