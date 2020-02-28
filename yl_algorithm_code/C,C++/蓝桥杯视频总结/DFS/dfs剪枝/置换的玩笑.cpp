#include <iostream>
#include <string>

using namespace std;

string s;
int n;
int ans[100]; 
bool vis[100];
bool ok;

// u表示考虑到了字符串的哪一位  cnt 表示 分出来了多少个数 
void dfs(int u, int cnt){
	if(ok){
		return; 
	}
	if(u == s.size()){
		for(int i = 0;i<cnt;i++){
			cout << ans[i] << " "; 
		}
		cout <<endl;
		ok = true;
		return ;
	}
	int x = s[u] - '0';  // 字符串拆一位出来 
	if(x<=n && !vis[x]){
		ans[cnt] = x;
		vis[x] = true;
		dfs(u+1, cnt +1);
		vis[x] = false;
	}
	if(u+1 >=s.size()){  // 拆两个的前提是当前长度+1要小于字符串的长度 
		return ;
	}
	x = x * 10 + s[u+1] - '0';// 字符串拆二位出来 
	if(x<=n && !vis[x]){
		ans[cnt] = x;
		vis[x] = true;
		dfs(u+2, cnt +1);
		vis[x] = false;
	}
}

int main(){
	cin >> s;
	
	n = s.size() <= 9 ? s.size() : (s.size()-9)/2 + 9;
	dfs(0,0);
	
	return 0;
}
/*
姐姐的实验报告.上原本记录着从 1到 n的序列,
任意两个数字间用空格间隔。但是“坑姐”的蒜头
居然把数字间的空格都给删掉了，整个数字序列变
成-一个长度为1到100的且首部没有空格的数字
串。
现在姐姐已经怒了，蒜头找你写个程序快点把试验
数据复原。

输入格式
输入文件有一行，为一个字符串一被蒜头搞乱的
实验数据。
字符串的长度在1到100之间。

输出格式
输出共一行，为姐姐的原始测试数据一1 到n的
输出。
任意两个数据之间有-个空格。
如果有多组符合要求的正确解，输出其中任意-组
即可。

4111109876532

4 1 11 10 9 8 7 6 5 3 2


*/ 



























