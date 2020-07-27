#include<iostream>
#include<cstring>
using namespace std;

int main() {
	int n,cnt=0;
	string s,ss[1005];
	cin >> n;
	getchar();
	getline(cin,s);
	int len = s.length();
	int w = (len % n == 0) ?  len / n : (len / n) + 1;
	for(int i=w-1; i>=0; i--) {
		for(int j=0; j<n; j++) {
			if(cnt<s.length()) {
				ss[j][i]=s[cnt++];
			} else {
				ss[j][i]=' ';  // 长度超出补空格 不然下标越界
			}
		}
	}
	for(int i=0; i<n; i++) {
		for(int j=0; j<w; j++) {
			cout << ss[i][j];
		}
		cout << endl;
	}
	return 0;
}
