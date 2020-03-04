#include <iostream>
#include <map>
using namespace std;

map<int,int> m;

// 一直80分，百度一看， 错的两个样例是因为 n<0 不用输出 

int main (){
	int n,x,max_cnt = 0,min_num = 0x3f3f3f;
	cin >> n;
	if(n>0){
		for(int i=0;i<n;i++){
		cin >> x;
		if(m.count(x) == 0){
			m[x] = 1;
		}else{
			m[x] += 1;
		}
		if(m[x] > max_cnt){
			max_cnt = m[x];
			min_num = x;
		}
	}
	cout << min_num;
	}
	return 0;
}
/*
编写一个程序，读入一组整数，这组整数是按照从小到大的顺序排列的，它
们的个数N也是由用户输入的，最多不会超过20。然后程序将对这个数组进行统计，
把出现次数最多的那个数组元素值打印出来。如果有两个元素值出现的次数相同，
即并列第一，那么只打印比较小的那个值。
输入格式：第一行是一个整数N，N? ￡? 20；接下来有N行，每一行表示一个整数，并且按照从小到大的顺序排列。
输出格式：输出只有一行，即出现次数最多的那个元素值。
*/
