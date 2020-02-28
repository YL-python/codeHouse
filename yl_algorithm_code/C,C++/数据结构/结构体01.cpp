#include <iostream>
#include <string>
using namespace std;

struct Student{
	string name;
	int score;
	Student(){
	}
	Student(string str, int n){
		name = str;
		score = n;
	}
}; 

int main(){
	Student a("nili",55);
	Student b = Student("wangwu",99);
	
	Student c;
	c.name = "zaoliu";
	c.score = 100;
	
	cout << a.name << endl << a.score << endl;
	cout << "----------------" << endl;
	cout << b.name << endl << b.score << endl;
	cout << "----------------" << endl;
	cout << c.name << endl << c.score << endl;
	return 0;
}

