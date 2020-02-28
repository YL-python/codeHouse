#include <iostream>
#include <string>
#include <stack> 
using namespace std;

stack<char > ss;

int main(){
	string str;
	getline(cin,str);
	
	int f = 1;
	
	for(int i=0; i<str.length(); i++){
		switch(str[i]){
			case '(':
				ss.push('(');
				break;
			case '{':
				ss.push('{');
				break;
			case '[':
				ss.push('[');
				break;
			case '<':
				ss.push('<');
				break;
			case ')':
				if(!ss.empty() && ss.top()=='('){
					ss.pop();
				}else{
					f = 0;
				}
				break;
			case '}':
				if(!ss.empty() && ss.top()=='}'){
					ss.pop();
				}else{
					f = 0;
				}
				break;
			case ']':
				if(!ss.empty() && ss.top()==']('){
					ss.pop();
				}else{
					f = 0;
				}
				break;
			case '>':
				if(!ss.empty() && ss.top()=='>'){
					ss.pop();
				}else{
					f = 0;
				}
				break;
		}
	}
	
	if(ss.empty() && f==1){
		cout << "����  ƥ��" << endl;
	}else{
		cout << "������  ƥ��" << endl;
	}
	
	
	return 0;
}




























