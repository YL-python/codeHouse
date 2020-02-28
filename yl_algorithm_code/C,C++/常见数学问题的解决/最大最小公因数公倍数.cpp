#include <iostream>
#include <string>
using namespace std;

//最小公倍数 = 两数相乘 除以 最大公约数 

int gcd(int x, int y){
    while(y^=x^=y^=x%=y);
    return x;
}

int lcm(int a,int b){
// 这个写法比a*b/gcd(a,b)要好 
	return a/gcd(a,b)*b;  
} 

int main(){
	int a=5,b=2;
	cout << gcd(a,b)<<endl;
	cout << lcm(a,b);
	return 0;
}

/*

#最大公因数普通算法
int gcd(int m,int n)
{    
    int t,r;    
    if (m<n)//为了确保是大数除小数    
    {        
        t=m;        
        m=n;       
        n=t;    
    }    
 
    while((m%n)!=0)//辗转相除    
    {        
        r=m%n;        
        m=n;        
        n=r;    
    }   
 
    return n;
}

//求最大公因数递归算法
int gcd(int x, int y){	
	if (y)			
        return gcd(y, x%y);		
    else			
        return x;
    // return y?gcd(y,x%y):x;
} 


#最美妙的最大公因数算法
int gcd(int x, int y){
    while(y^=x^=y^=x%=y);
    return x;
}
*/
