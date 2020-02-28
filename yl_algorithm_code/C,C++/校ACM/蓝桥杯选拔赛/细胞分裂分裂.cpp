#include <iostream>
#include <string>
using namespace std;

int gcd(int x, int y){
    while(y^=x^=y^=x%=y);
    return x;
}

int lcm(int a,int b){
	return a/gcd(a,b)*b;
}

int main(){
	int a,b;
	cin >>a>>b;
	int m=0;
	for(int i=1;i<1000000;i++){
		m=lcm(a,b);
		m%2==0?a+=1:a+=a;
//		cout << "m="<<m<<endl; 
		if(a>=b){
			cout<<i;
			break;
		}
	} 
	return 0;
}


/*
Description

�����Ǹ���ֵ�ϸ����Ӫ��Һ��������ϸ����������С�������������Ļ���ϸ���ͻ���ѳ�Ϊԭ����2���������ż���Ļ���ϸ��������ֻ���1����ÿ�����Ӫ��Һ������ͬ�ģ���������֪��a��ϸ����һ����������Һ�������ٶ�����ϸ���������ܲ�����b����


Input
ֻ��һ�У�2��������a,b���ÿո������0<a<b<=2e9��


Output
���ϸ������������b������Ҫ�����졣


Sample Input 1 

3 5
Sample Output 1

1
*/ 
