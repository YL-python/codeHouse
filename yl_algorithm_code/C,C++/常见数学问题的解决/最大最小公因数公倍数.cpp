#include <iostream>
#include <string>
using namespace std;

//��С������ = ������� ���� ���Լ�� 

int gcd(int x, int y){
    while(y^=x^=y^=x%=y);
    return x;
}

int lcm(int a,int b){
// ���д����a*b/gcd(a,b)Ҫ�� 
	return a/gcd(a,b)*b;  
} 

int main(){
	int a=5,b=2;
	cout << gcd(a,b)<<endl;
	cout << lcm(a,b);
	return 0;
}

/*

#���������ͨ�㷨
int gcd(int m,int n)
{    
    int t,r;    
    if (m<n)//Ϊ��ȷ���Ǵ�����С��    
    {        
        t=m;        
        m=n;       
        n=t;    
    }    
 
    while((m%n)!=0)//շת���    
    {        
        r=m%n;        
        m=n;        
        n=r;    
    }   
 
    return n;
}

//����������ݹ��㷨
int gcd(int x, int y){	
	if (y)			
        return gcd(y, x%y);		
    else			
        return x;
    // return y?gcd(y,x%y):x;
} 


#���������������㷨
int gcd(int x, int y){
    while(y^=x^=y^=x%=y);
    return x;
}
*/
