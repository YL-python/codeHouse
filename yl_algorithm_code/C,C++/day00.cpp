#include <iostream>
#include <string> 
using namespace std;  // ��Ĭ�ϵ������ռ�  

namespace mystd{  // �Զ��������ռ� 
	void sort(){
		cout << "nihaoya" << endl;
	}
} 

// ������ָ��ͬһ����ַ  ָ���ǿ������ڴ�ռ�洢ָ��ĵ�ַ 

template<typename T>
T sum(T a,T b){
	return NULL;
} // �Զ����������� 


int main(){
	mystd::sort(); // ʹ�������ռ��ڵ����� 
	
	cout << "HelloWorld!" << endl;
	
	int a;
	char b;
	float c;
	
	cin >> a;
	cin >> b; // �����ַ� ����97������a  
	cin >> c;
	
	cout << a << endl << b << endl << c << endl;
	
//	system("pause");

	class Student{  // ����ѧ���� 
		public: // ���� �� ���� 
			char *name;
			int age;
			float score;
		public:  //  ���� �� ����
			void say(){
				printf("%s��������%d,�ɼ���%f\n",name,age,score);
			} 
	};
	
	Student stu;  // �������� 
	stu.name = "С��";
	stu.age = 18;
	stu.score = 92.5f;
	stu.say();
	
	// String ��ʹ��
	string s1;
	string s2 = "c puls puls";
	string s3 = s2;
	string s4(5,'s');
	int len = s2.length();
	
	return 0;
}
