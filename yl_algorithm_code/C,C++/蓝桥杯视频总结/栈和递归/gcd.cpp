#include <iostream>
#include <string>

using namespace std;

int gcd(int x,int y){
	return y?gcd(y,x%y):x;
	/*
	if(y == 0){
		return x
	}else{
		return gcd(y,x%y);
	}
	*/
}

int main(){
	
	
	
	return 0;
}
/*
		   | f(y,x%y)  y>0 
f(x, y) =  |
		   | x         y=0
*/



























