#include <iostream>
using namespace std;

const int DAY = 1000;

int main() {
	int yyyy = 2014;
	int mm = 11;
	int dd = 9;
	for(int i=1; i<=DAY; i++) {
		dd++;
		if(dd == 30 && mm == 2) {
			if(yyyy % 400 == 0 || (yyyy % 4== 0 && yyyy % 100 != 0)) {
				// 闰年 
				dd = 1;
				mm = 3; 
			}else{
				dd = 2;
				mm = 3;
			}
		}
		if(dd == 31 && (mm == 4 || mm == 6 || mm == 9 || mm == 11)){
			mm ++;
			dd = 1;
		}
		if(dd == 32 && (mm == 1 || mm == 3 || mm == 5 || mm == 7 || mm == 8 || mm == 10 || mm == 12)){
			mm ++;
			dd = 1;
		}
		if(mm == 13){
			yyyy ++;
			mm = 1;
		}
	}
	cout << yyyy << "-" << mm << "-" << dd << endl;
	return 0;
}

/*
星系炸弹

在X星系的广袤空间中漂浮着许多X星人造“炸弹”，用来作为宇宙中的路标。
每个炸弹都可以设定多少天之后爆炸。
比如：阿尔法炸弹2015年1月1日放置，定时为15天，则它在2015年1月16日爆炸。
有一个贝塔炸弹，2014年11月9日放置，定时为1000天，请你计算它爆炸的准确日期。

请填写该日期，格式为 yyyy-mm-dd  即4位年份2位月份2位日期。比如：2015-02-19
请严格按照格式书写。不能出现其它文字或符号。
*/

