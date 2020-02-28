#include <iostream>
#include <string>
using namespace std;

int only(int x){
	int ans=0;
	while(x>=10){
		ans+=x%10;
		x/=10;
	}
	ans+=x;
	return ans;
}

int main(){
	int n,m;
	cin >>n;
	for(int i=0;i<n;i++){
		cin >>m;
		while(m>=10){
			m = only(m);
		}
		cout << m << endl;
	} 
	return 0;
}
/*
Description
��һ����1�������� t(1<=t<=1000)��t�������������������ÿ��һ��n(0<n<1000000)�����n> 10�������n�ĸ���λ����ֵ��ӣ������ӵĺ�ans������10���������˲�����ֱ��ans <10 ���������
����n = 1234����1 + 2 + 3 + 4 = 10���ظ����������1 + 0 = 1 <10������Ľ��Ϊ1

Input
��һ������һ��������t
������t��ÿ��һ��������n��0<n<1000000��

Output
ÿ��n��Ӧһ���������һ��С��10

Sample Input 1 
4
1234
123
12345
1

Sample Output 1
1
6
6
1
*/ 
