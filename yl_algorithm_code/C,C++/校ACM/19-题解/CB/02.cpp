#include <iostream>
using namespace std;

void jinzhi(int x){
	// 先想想 一个数 取10 进制上的每一位 我们是怎么操作 
	while(x!=0){
		/*
		cout << x%10;
		x/=10;
		输出结果是 9102 
		*/
		// 现在来写26 进制
		char s = x%26-1+'A';
		// 减一是因为 1是 A  而 %26最小值是0 
		cout << s;
		x/=26; 
		// 输出 QYB 
	}
}

int main(){
	// 类似 26 进制
	jinzhi(2019);
	return 0;
} 
/*
小明用字母 A 对应数字 1，B 对应 2，以此类推，用 Z 对应 26。对于 27
 以上的数字，小明用两位或更长位的字符串来对应，例如 AA 对应 27，AB 对
 应 28，AZ 对应 52，LQ 对应 329。
 请问 2019 对应的字符串是什么？
*/ 
