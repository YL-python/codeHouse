#include <iostream>
#include <string>
#include <set>   // set ͷ�ļ� 
using namespace std;

int main(){
	set<int> a;  // set ���ϲ������ظ�Ԫ��  ���һ��Զ����� 
	
	a.insert(0); 
	a.insert(1); 
	a.insert(2);  // insert() ���뷽�� 
	a.insert(2);  // �����ظ� 
	
	a.erase(0);  // ɾ��Ԫ��   �����ڵ�ʱ�򲻽��в��� û�б��� 

	cout << a.count(1) << endl;  // ����Ԫ��  �ҵ�����  1  û�ҵ����� 0	
	
	// ������Ҫ�õ�������  д���̶ܹ� 
	for(set<int>::iterator i=a.begin(); i != a.end(); i++){
		cout << *i <<endl ;
	} 
	
	a.clear();  // ��ռ��� ͬʱ������ڴ� 
	
	/*  set  �ײ�ʵ��ԭ���� ����� 
	insert()  ��   O(logn)
	erase()  ɾ   O(logn)
	count()  ͳ�Ƹ���    O(logn)
	size()  ��ȡԪ�ظ���    O(1)
	clear()   ���    O(n)
	*/ 
	
	return 0;
}

