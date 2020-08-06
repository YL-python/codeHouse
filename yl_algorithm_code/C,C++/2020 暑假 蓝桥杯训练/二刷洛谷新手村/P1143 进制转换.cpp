#include <iostream>
#include <cstring>
using namespace std;

int n,m,ten,cnt;
string num;
string int2str="0123456789ABCDEF",ans;

int str2int(char c) {
	if(c>='A'&&c<='F')
		return c - 'A' + 10;
	if(c>='0'&&c<='9')
		return c-'0';
}

int main() {
	cin >> n >> num >> m;
	// n 进制转 10 进制
	for(int i=0; i<num.length(); i++) {
		ten = ten*n + str2int(num[i]);
	}
	// 10 进制转 m 进制
	while(ten) {
		ans[cnt++] = int2str[ten % m];
		ten /= m;
	}
	// 字符串反转
	for(int i=cnt-1; i>=0; i--) {
		cout << ans[i];
	}
	return 0;
}
