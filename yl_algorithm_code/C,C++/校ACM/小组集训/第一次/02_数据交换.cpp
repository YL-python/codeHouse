#include <iostream>
using namespace std;

void swap(int &a, int &b) {
	int t = a;
	a = b;
	b = t;
}

int main () {
	int a, b;
	cin >> a >> b;
	swap(a, b);
	cout << a << " " << b;
	return 0;
}
/*
问题描述
　　编写一个程序，输入两个整数，分别存放在变量x和y当中，然后使用自己定义的函数swap来交换这两个变量的值。
　　输入格式：输入只有一行，包括两个整数。
　　输出格式：输出只有一行，也是两个整数，即交换以后的结果。
　　要求：主函数负责数据的输入与输出，但不能直接交换这两个变量的值，
	必须通过调用单独定义的函数swap来完成，而swap函数只负责交换变量的值，不能输出交换后的结果。
*/
