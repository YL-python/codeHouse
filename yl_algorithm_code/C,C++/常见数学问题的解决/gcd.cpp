#include<bits/stdc++.h>  // ����ͷ�ļ� 
using namespace std;

// ������� 
int gcd(int a,int b){     
    return b?gcd(b,a%b):a;    //�ݹ鷨�����Լ��
}

// ��С������ 
int lcm(int a,int b){
	// ���д����a*b/gcd(a,b)Ҫ�� 
	return a/gcd(a,b)*b;  
} 

int main(){
	int a, b;
	cin >> a >> b;
	cout << gcd(a,b);
	
	return 0;
}
