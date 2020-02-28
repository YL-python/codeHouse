#include <iostream>
#include <string>
#include <vector> 
using namespace std;

// 定义一维数组长度10005  每一个装一个动态数组 
// 其实就是二维动态数组  只不过有一维大小确定了 
// 这样写更好  vector 的底层实现原理 
vector<int> a[10005]; 
int n,m; 
/* 
一个矩阵，n行 m个元素 每一行的元素都不相同叫锯齿矩阵 
1 12 2 2
1 2 3
4 7 0 8 11 
每一行的长度不固定用vertor来装 
*/ 
int main(){
	int x,y;
	cin >> n >> m; 

	for(int i=0;i<m;i++){
		cin >> x >> y;
		a[x].push_back(y);
	}
	
	for(int i=1;i<=n;i++){
		for(int j=0;j<a.size();j++){
			cout << a[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}

