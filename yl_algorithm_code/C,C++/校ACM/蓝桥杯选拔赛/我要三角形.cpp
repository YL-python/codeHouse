#include <iostream>
#include <string>
using namespace std;

int a,b,c,t; 
 
int main(){
	cin >> a >> b >> c;
	if(a>b){
		t=a;
		a=b;
		b=t;
	}
	if(a>c){
		t=a;
		a=c;
		c=t;
	}
	if(b>c){
		t=b;
		b=c;
		c=t;
	}
//	cout << a<<b<<c<<endl;
	if(a+b>c&&c-b<a){
		cout << "YES";
	}else{
		cout << "NO";
	}
	
	return 0;
}
/*
Description

现在给你3个正整数，判断是否能构成三角形



Input
3个正整数，用空格隔开


Output
如果能构成三角形，输出‘YES’，否则输出‘NO’


Sample Input 1 

3 4 5
Sample Output 1

YES
Sample Input 2 

1 2 3
Sample Output 2

NO
Sample Input 3 

3 3 3
Sample Output 3

YES
*/
