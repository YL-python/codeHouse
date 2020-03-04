#include <iostream>
using namespace std;

int *GetTwoInts(){
	int a[2];
	cin >> a[0] >> a[1];
	return a;
} 

int main (){
	// 指针是地址   * 是取地址值 
	int *a;
	a = GetTwoInts();
	cout << *a + *(a+1);
	return 0;
}
/*
你的表妹正在学习整数的加法，请编写一个程序来帮助她学习。
该程序调用了一个函数GetTwoInts，由它来返回两个从键盘读入的100以内的整数，
然后计算这两个整数之和，并把答案显示出来。要求：在主函数中不能使用scanf等函数直接输入这两个整数，
而必须通过调用GetTwoInts函数来完成，在GetTwoInts函数中可以使用scanf函数。
另外，由于该函数必须同时返回两个整数，因此不能采用函数返回值的方式，而必须采用指针的方法来实现。
　　输入格式：输入只有一行，即两个100以内的整数。
　　输出格式：输出只有一行，即这两个整数之和。
*/
