#include <iostream>
#include <string>
#include <vector>
using namespace std;

// vector动态数组  需要 vector 头文件
// 定义： vector<T> vec   定义了类型是 T的名字为vec的动态数组

int main() {
	vector<int> v;
	// push_back()  向vector数组最后面插入一个元素
	v.push_back(0);
	v.push_back(1);
	v.push_back(2); // [1,2,3]

	// size()方法获取动态数组的长度
	for(int i = 0; i < v.size(); i++) {
		cout << "v[" << i << "]=" << v[i] << endl;
	}
	cout << "------------------" << endl;

	// 修改元素可以直接赋值，不能超界
	v[0] = 2;
	v[1] = 1;
	v[2] = 0;
	for(int i = 0; i < v.size(); i++) {
		cout << "v[" << i << "]=" << v[i] << endl;
	}
	cout << "------------------" << endl;

	// pop_back() 删除数组最后一个元素的方法
	v.pop_back();
	
	for(int i = 0; i < v.size(); i++) {
		cout << "v[" << i << "]=" << v[i] << endl;
	}
	cout << "------------------" << endl;

	// 只支持在尾部进行操作 为了把时间复杂度变成 o(1)

	// 清空
	// 方法1 clear()方法  会清空数据但是不会清空内存
	v.clear();
	// 方法2 新建一个vector数组去替换旧数组
	vector<int>().swap(v);


	// 构造函数
	vector<int> v1(10,1); // 创建长度是10 ，值全为 1的动态数组	
	vector<int> v2(10);  // 创建长度是10 ，值全为 0的动态数组	
	
	
	// 二维vector数组
	vector<vector<int> > vec2;  // 空格要写
	// vec2[0]; // 这样写是违法的 需要先把第一维度撑开  
	for(int i=0;i<3;i++){
		vector<int> x(i+1,1);  // 先把第一维度撑开 
		vec2.push_back(x);  // 把一维度装到vec2里面 
	} 
	for(int i=0;i<3;i++){
		for(int j=0;j<=i;j++){
			cout << vec2[i][j] << " " ;
		}
		cout << endl;
	} 
	cout << "------------------" << endl;
	
	// 构造 n行 m列为 0的动态数组 
	vector<vector<int> > vec3(n, vector<int>(m, 0));
	 
	
	return 0;
}

























































