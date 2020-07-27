#include<iostream>
#include<string>
using namespace std;

// 传一个字符串，吧字符串转成数字，不能转的返回 0
// 题目给定 AB的范围是   [1,1000]
int str2int(string s) {
	int len = s.length();
	int num = 0;
	for(int i=0; i<len; i++) {
		if(s[i] >= '0' && s[i] <= '9') {
			num*=10;
			num += s[i] - '0';
		} else {
			return 0;
		}
	}
	if(num > 1000){
		return 0;
	}else{
		return num;
	}
}

int main() {

	string stra, strb;
	int numa, numb;

	// 难在这个输入了
	// 两个字符串以第一个空格分隔 第二个字符串会有空格
	// 123 123 a   这样的 B是 123 a  
	cin >> stra;
	getchar();  // 吃掉第一个空格 
	getline(cin,strb);
	
	// 不吃空格的话  strb[0]是空格 
	// cout << strb[0] << endl << strb.length() << endl; 

	numa = str2int(stra);
	numb = str2int(strb);

	int flag = 0;
	if(numa == 0) {
		cout << "?";
		flag = 1;
	} else {
		cout << numa;
	}
	cout << " + ";
	if(numb == 0) {
		cout << "?";
		flag = 1;
	} else {
		cout << numb;
	}
	cout << " = ";
	if(flag) {
		cout << "?";
	} else {
		cout << numa+numb;
	}
	return 0;
}
