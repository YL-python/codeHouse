#include <iostream>
#include <string>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=i;j++){
			printf("%d*%d=%d ",j,i,i*j);
		}
		cout << endl;
	} 
	return 0;
}
/*
Description

给你一个正整数n，打印n*n的乘法表。（n<=20）


Input
输入一个数字n


Output
输出对应的乘法表，每个等式之间用空格隔开


Sample Input 1 

8
Sample Output 1

1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
1*4=4 2*4=8 3*4=12 4*4=16
1*5=5 2*5=10 3*5=15 4*5=20 5*5=25
1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36
1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49
1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64
*/ 
