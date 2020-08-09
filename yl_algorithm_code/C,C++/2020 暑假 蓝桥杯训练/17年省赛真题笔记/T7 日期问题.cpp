#include <iostream>
#include <set>
#include <sstream>
using namespace std;
int a,b,c;

int isLeap(int year) {
	if( (year%400 == 0) || (year%4==0&&year%100!=0) ) {
		return 1;
	} else {
		return 0;
	}
}

void i2s(int i,string &s) {
	stringstream ss;
	ss << i;
	ss >> s;
}

string fun(int a,int b,int c) {
	if(a >= 0 && a <= 59) {
		a+=2000;
	} else if(a > 59 && a < 100) {
		a+=1900;
	} else {
		return "";
	}
	if(b <1 || b>12) return "";
	if(c <1 || c>31) return "";
	int temp = 28 + isLeap(b);
	switch(b) {
		case 2:
			if(c>temp ) return "";
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			if(c > 30) return "";
	}
	string _a,_b,_c;
	i2s(a,_a);
	i2s(b,_b);
	i2s(c,_c);
	if(_b.length() == 1) _b="0" + _b;
	if(_c.length() == 1) _c="0" + _c;
	return _a + "-" + _b + "-" + _c;
}
int main() {
	string s;
	cin >> s;
	a = (s[0] - '0')*10 + s[1] - '0';
	b = (s[3] - '0')*10 + s[4] - '0';
	c = (s[6] - '0')*10 + s[7] - '0';
	string s1 = fun(a,b,c);
	string s2 = fun(b,c,a);
	string s3 = fun(c,b,a);
	set<string> ans;
	if(s1 != "")ans.insert(s1);
	if(s2 != "")ans.insert(s2);
	if(s3 != "")ans.insert(s3);
	for(set<string>::iterator i=ans.begin(); i!=ans.end(); i++) {
		cout << *i << endl;
	}
	return 0;
}
/*
日期都在1960年1月1日至2059年12月31日
年/月/日
月/日/年
日/月/年

样例输入
02/03/04

样例输出
2002-03-04
2004-02-03
2004-03-02
*/
