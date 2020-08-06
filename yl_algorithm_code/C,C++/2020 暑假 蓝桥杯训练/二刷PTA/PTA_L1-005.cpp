#include<iostream>
#include<string>
using namespace std;

/* 参数说明
str: 输入的个人信息， sj：输入的试机号码，zk：输入的准考座位号码 
n,m题目的，cnt是输入m后输入的 查询 试机号码

用了一点数据结构或者说一种巧的方法吧 
strList：下标是 试机号码，值是 对应人的身份证号 
vis： 下标是 试机号码，值是 对应人的准考座位号码 

思路很多 可以存到数组里面遍历，然后if判断输出
我这样的写法就是牺牲空间赚取时间吧 
*/
string strList[1005],str;
int vis[1005];
int n,m,cnt,sj,zk;

int main() {
	cin >> n;
	while(n--){
		cin >> str >> sj >> zk;
		strList[sj] = str;
		vis[sj] = zk;
	}
	cin >> m;
	while(m--){
		cin >> cnt;
		cout << strList[cnt] << " " << vis[cnt] << endl;
	}
	return 0;
}
