#include <iostream>
#include <string>
#include <map>
#include <utility>  // pair ��ͷ�ļ� 
using namespace std;

int main(){
	
	map<string,int> dict;
	
//	make_pair(v1,v2)  ��v1,v2����һ�� �����ڹ����ṹ�� 
	dict.insert(make_pair("tom",1));
	dict.insert(make_pair("Jone",2));
	dict.insert(make_pair("mark",3));
	dict.insert(make_pair("tom",3));  // ����key��ͬ�Ĳ����滻���൱��û�в��� 
	
	// ����ֵ�͸���ֵ  Ҳ����ֱ�������ַ�������ʼ�� ����pair 
	// �����Ƽ����ַ�������ʼ�� 
	cout << dict["tom"] << endl; 
	dict["tom"] = 33; 
	cout << dict["tom"] << endl; 
	
	// count() ��������key�Ƿ����
	int c_tom = dict.count("tom"); 
	cout << c_tom <<endl;
	int c_aaa = dict.count("aaa"); 
	cout << c_aaa <<endl;
	
	// ������ ������
	for(map<string,int>::iterator i=dict.begin(); i != dict.end(); i++){
		cout << (*i).first << "->" << i->second << endl;
	}
	
	// clear()  ��գ�������ڴ� 
	
	// map �� map  map �� set 
	
	return 0;
}

