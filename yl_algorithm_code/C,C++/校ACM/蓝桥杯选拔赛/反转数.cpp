#include <iostream>
#include <string.h>
using namespace std;

int n,a[10000];
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	for(int i=0;i<n;i++){
		int ans=0,x=a[i];
		while(x){
			ans = ans*10 + (x%10);
			x/=10;
		}
		cout << ans<<endl;
	}
	return 0;
}
/*
Description
�뽫һ����������ת�������ת֮��ǰ����0����ȥ���������

Input
��һ��Ϊһ��T ������T���������T��ÿ��һ��n(n<=100000)��

Output
���n��ת֮��Ĵ�

Sample Input 1 
2
66
660

Sample Output 1
66
66
*/
