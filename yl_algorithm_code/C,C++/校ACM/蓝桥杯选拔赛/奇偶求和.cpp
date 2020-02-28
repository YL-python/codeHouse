#include <iostream>
#include <string>
using namespace std;

int count,n[10005],d[10005];
float a[10005][10005],sum0,sum1;

int main(){
	cin >> count;
	for(int i=0;i<count;i++){
		cin >> n[i] >> d[i];
		sum0=0.0,sum1=0.0;
		for(int j=1;j<=n[i];j++){
			cin >> a[i][j];
			if(j%2 == 0){
				sum0 += a[i][j];
			}else{
				sum1 += a[i][j];
			}
		}
//		printf("sum0=%f\nsum1=%f\n",sum0,sum1);
		if(d[i] == 0){
			if(int(sum0) == sum0){
				printf("%d\n",int(sum0));
			}else{
				printf("%.2f\n",sum0);
			}	
		}else if(d[i] == 1){
			if(int(sum1) == sum1){
				printf("%d\n",int(sum1));
			}else{
				printf("%.2f\n",sum1);
			}
		}else{
			cout << "Welcome to Nanli ACM/ICPC!" << endl;
		}
	}
	return 0;
}
/*
奇偶求和
Description

给你一组数，请求它们中一些数的和。


Input
第一行为一个数，代表测试数据的组数。随后T组数据，每组数据第一行为一个n和d(d为整数)，第二行为n个数（每个数下标从1开始，然后依次增加）。如果d为1请求出所有下标为奇数的和，如果d为0请求出所有下标为偶数的和。


Output
输出有T行，每行一个答案，如果答案是一个整数请不要输出小数，如果不是请保留2位小数输出。如果d不等0或1，输出Welcome to Nanli ACM/ICPC!


Sample Input 1 

1
8 1
1 2 3 4 5 6 7 8
Sample Output 1

16
*/
