#include <iostream>
#include <string>
using namespace std;

int gcd(int a, int b){
    return b?gcd(b,a%b):a;
}

int lcm(int a,int b){
	return a/gcd(a,b)*b;
}


int main(){
	int a,n;
	cin >> a >> n;
	int ans=1,m=0;
	for(int i=0;i<n;i++){
		if(a>ans){
			m = lcm(a,ans);
		}else{
			m = lcm(ans,a);
		}
		if(m%2 == 0){
			ans+=1;
		}else{
			ans+=ans;
		}
	}
	cout << ans;
	return 0;
}
/*
Description

����������һ��ϸ����ÿ������̶�������Ӫ��Һ������ʱ�̹۲�ϸ���������������˼���Ĺ۲��㷢��������ϸ����һ����ֵ�����Ӫ��Һ��������ϸ����������С�������������Ļ���ϸ���ͻ���ѳ�Ϊԭ����2���������ż���Ļ���ϸ��������ֻ���1������������֪��1��ϸ����a��������Ӫ��Һ�£���n���ϸ�������Ƕ��١�


Input
ֻ��һ�У�2��������a��n�ÿո�ֿ���(a<=100,n<=20)


Output
�����Ӧ������


Sample Input 1 

5 3
Sample Output 1

6
*/ 
