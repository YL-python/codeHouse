#include <iostream>
#include <string>
using namespace std;

string s; 

int main(){
	getline(cin,s);
	int len = s.length();
	int flag = 0;
	for(int i=0;i<len;i++){
		if(s[i] == '.'){
			flag=1;
		}
	}
	if(!flag){
		cout << "整数"; 
	}else{
		cout << "小数"; 
	} 
	return 0;
}
/*
Description

给你一个正数，判断是小数还是整数（一定是合法的数字）



Input
一个数字，小于1000



Output
如果是小数，输出'小数'，如果是整数则输出'整数'


Sample Input 1 

1.3
Sample Output 1

小数
Sample Input 2 

5
Sample Output 2

整数
Sample Input 3 

3.0
Sample Output 3

小数
*/
