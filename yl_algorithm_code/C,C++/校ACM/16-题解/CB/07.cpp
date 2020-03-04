#include <iostream>
#include <set>
#include <string>
using namespace std;
// ֱ��DFS �в�ͨ���������T ���е����
// ����ö��  ��

int a[] = {0,0,0,0,0,0,0,1,1,1,1,1};
int ans=0;
int map[3][4];

set<string> s;

void dfs(int i, int j) {
	map[i][j] = 0;
	if(i-1>=0 && map[i-1][j] == 1) {
		dfs(i-1, j);
	}
	if(i+1<=2 && map[i+1][j] == 1) {
		dfs(i+1, j);
	}
	if(j-1>=0 && map[i][j-1] == 1) {
		dfs(i, j-1);
	}
	if(j+1<=3 && map[i][j+1] == 1) {
		dfs(i, j+1);
	}
}

bool check() {
	// һά���ά
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			map[i][j] = a[i*4+j];
		}
	}
	// dfs��ͨ�Լ���
	int cnt = 0; // ��ͨ��ĸ���
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			if(map[i][j] == 1) {
				dfs(i, j);
				cnt ++;
			}
		}
	}
	return cnt == 1;
}

void a2str(string &str){
	for(int i=0;i<12;i++){
		str.insert(str.end(), a[i]+'0');
	}
}

bool can(){
	// ������һ�ε�������û���ظ�
	string a_str;
	a2str(a_str);
	if(s.count(a_str)){
		cout << "cf" << endl;
		return false;
	}else{
		s.insert(a_str);
		cout << a_str << endl;
		return true;
	}
}

// ȫ����
void f(int k) {
	if(k == 12 && can()) {
		if(check()) {
			ans++;
		}
	}
	for(int i=k; i<12; i++) {
		{
			int t = a[i];
			a[i] = a[k];
			a[k] = t;
		}
		f(k+1);
		{
			int t = a[i];
			a[i] = a[k];
			a[k] = t;
		}
	}
}

int main() {
	f(0);
	cout << ans << endl;
	return 0;
}

/*

����Ʊ

�硾ͼ1.jpg��, ��12������һ���12��Ф����Ʊ��
������Ҫ���м���5������Ҫ����������ŵġ�
����������һ���ǲ���������
���磬��ͼ2.jpg������ͼ3.jpg���У��ۺ�ɫ��ʾ���־��Ǻϸ�ļ�ȡ��

������㣬һ���ж����ֲ�ͬ�ļ�ȡ������

����д��ʾ������Ŀ��������
ע�⣺���ύ��Ӧ����һ����������Ҫ��д�κζ�������ݻ�˵�������֡�

*/
