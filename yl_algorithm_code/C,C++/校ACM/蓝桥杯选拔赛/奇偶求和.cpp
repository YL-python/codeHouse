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
��ż���
Description

����һ����������������һЩ���ĺ͡�


Input
��һ��Ϊһ����������������ݵ����������T�����ݣ�ÿ�����ݵ�һ��Ϊһ��n��d(dΪ����)���ڶ���Ϊn������ÿ�����±��1��ʼ��Ȼ���������ӣ������dΪ1����������±�Ϊ�����ĺͣ����dΪ0����������±�Ϊż���ĺ͡�


Output
�����T�У�ÿ��һ���𰸣��������һ�������벻Ҫ���С������������뱣��2λС����������d����0��1�����Welcome to Nanli ACM/ICPC!


Sample Input 1 

1
8 1
1 2 3 4 5 6 7 8
Sample Output 1

16
*/
