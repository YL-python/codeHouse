#include <iostream>
#include <string>

using namespace std;

// 2 ÊÇËØÊı 
bool ss(int a){
    for(int i=2;i*i<=a;i++)
        if(a%i==0)
            return false;
    return true;
}

int main(){
	
	cout << ss(2) << endl; 
	cout << ss(4) << endl; 
	cout << ss(5) << endl; 
	
	return 0;
}




























