#include<bits/stdc++.h>  // ����ͷ�ļ� 
using namespace std;

int gcd(int a,int b){     
    return b?gcd(b,a%b):a;    //�ݹ鷨�����Լ��
}
int main(){
	int a, b;
	cin >> a >> b;
	cout << gcd(a,b);
	
	return 0;
}
