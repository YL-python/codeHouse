#include <iostream>
#include <set>
#include <string>
using namespace std;
// 直接DFS 行不通，解决不了T 字行的情况
// 暴力枚举  巧

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
	// 一维变二维
	for(int i=0; i<3; i++) {
		for(int j=0; j<4; j++) {
			map[i][j] = a[i*4+j];
		}
	}
	// dfs连通性检验
	int cnt = 0; // 连通块的个数
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
	// 查找这一次的数组有没有重复
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

// 全排列
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

剪邮票

如【图1.jpg】, 有12张连在一起的12生肖的邮票。
现在你要从中剪下5张来，要求必须是连着的。
（仅仅连接一个角不算相连）
比如，【图2.jpg】，【图3.jpg】中，粉红色所示部分就是合格的剪取。

请你计算，一共有多少种不同的剪取方法。

请填写表示方案数目的整数。
注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。

*/
