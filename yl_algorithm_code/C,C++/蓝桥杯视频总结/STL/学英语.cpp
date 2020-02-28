#include <iostream>
#include <string>
#include <set>
using namespace std;

set<string> ss;


// string 类型中 length() 和 size()没有区别 
// char [] 中有区别 
int main(){
	int n,op;
	string str; 
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> op >> str;
		for(int j=0;j,str.size();j++){  
			if(str[j]>='A' && str[j]<='Z'){
				str[j] = 'a' + str[j] - 'A';
			}
		}
		if(op == 0){
			ss.insert(str);
		}else if(op == 1){
			if(ss.count(str)){
				cout << "YES" << endl;
			}else{
				cout << "NO" << endl;
			}
		}
	}
	return 0;
}
/*
输入整数和字符串
0表示学会了
1表示不清楚会不会
遇到1 就判断会不会并输出
不区分大小写 
*/

