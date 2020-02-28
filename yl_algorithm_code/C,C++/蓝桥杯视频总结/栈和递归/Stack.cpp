#include <iostream>
#include <string>
using namespace std;

struct Stack{
	int data[10000];
	int top = -1;
	
	void push(int x){
		top++;
		if(top < 10000){
			data[top] = x;
		}else{
			top --;
			cout << " Õ»Òç³ö£¡ " << endl;
		}
	}
	void pop(){
		if(top >= 0){
			top--;
		}
	}
	int topval(){
		if(top >= 0){
			return data[top];
		}
	}
};

int main(){
	
	Stack s;
	for(int i=1;i<=10;i++){
		s.push(i);
	}
	
	for(int i=1;i<=10;i++){
		cout << s.topval() << " " ;
		s.pop();
	}
	
	return 0;
}
















































