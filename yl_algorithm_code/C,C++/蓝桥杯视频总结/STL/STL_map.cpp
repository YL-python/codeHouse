#include <iostream>
#include <string>
#include <map>
#include <utility>  // pair 的头文件 
using namespace std;

int main(){
	
	map<string,int> dict;
	
//	make_pair(v1,v2)  把v1,v2绑定在一起 类似于构建结构体 
	dict.insert(make_pair("tom",1));
	dict.insert(make_pair("Jone",2));
	dict.insert(make_pair("mark",3));
	dict.insert(make_pair("tom",3));  // 插入key相同的不会替换，相当于没有插入 
	
	// 访问值和更改值  也可以直接用这种方法来初始化 不用pair 
	// 而且推荐这种方法来初始化 
	cout << dict["tom"] << endl; 
	dict["tom"] = 33; 
	cout << dict["tom"] << endl; 
	
	// count() 函数访问key是否存在
	int c_tom = dict.count("tom"); 
	cout << c_tom <<endl;
	int c_aaa = dict.count("aaa"); 
	cout << c_aaa <<endl;
	
	// 遍历用 迭代器
	for(map<string,int>::iterator i=dict.begin(); i != dict.end(); i++){
		cout << (*i).first << "->" << i->second << endl;
	}
	
	// clear()  清空，会清空内存 
	
	// map 套 map  map 套 set 
	
	return 0;
}

