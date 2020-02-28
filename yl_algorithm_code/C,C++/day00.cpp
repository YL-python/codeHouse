#include <iostream>
#include <string> 
using namespace std;  // 打开默认的命名空间  

namespace mystd{  // 自定义命名空间 
	void sort(){
		cout << "nihaoya" << endl;
	}
} 

// 引用是指向同一个地址  指针是开辟了内存空间存储指向的地址 

template<typename T>
T sum(T a,T b){
	return NULL;
} // 自定义数据类型 


int main(){
	mystd::sort(); // 使用命名空间内的内容 
	
	cout << "HelloWorld!" << endl;
	
	int a;
	char b;
	float c;
	
	cin >> a;
	cin >> b; // 单个字符 输入97不会变成a  
	cin >> c;
	
	cout << a << endl << b << endl << c << endl;
	
//	system("pause");

	class Student{  // 定义学生类 
		public: // 定义 类 变量 
			char *name;
			int age;
			float score;
		public:  //  定义 类 方法
			void say(){
				printf("%s的年龄是%d,成绩是%f\n",name,age,score);
			} 
	};
	
	Student stu;  // 创建对象 
	stu.name = "小明";
	stu.age = 18;
	stu.score = 92.5f;
	stu.say();
	
	// String 类使用
	string s1;
	string s2 = "c puls puls";
	string s3 = s2;
	string s4(5,'s');
	int len = s2.length();
	
	return 0;
}
