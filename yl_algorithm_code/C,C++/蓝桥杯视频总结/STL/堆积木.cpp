#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> v[10005];

int main(){
	int n,m,a,b;
	scanf("%d %d",&n,&m);
	for(int i=1;i<=n;i++){  // 编号从1 开始 
		v[i].push_back(i);
	}
	
	for(int i=0;i<m;i++){
		scanf("%d %d",&a,&b);
		if(a == b){  // 自己操作自己就很麻烦 本来也不需要操作 
			continue;
		}
		for(int j=0; j<v[b].size(); j++){
			v[a].push_back(v[b][j]);
		}
		vector<int>().swap(v[b]);// 清空一下b 的内存 
	}
	for(int i=1;i<n;i++){
		for(int j=0;j<v[i].size();j++){
			if(j!=v[i].size()){  // 控制结尾的空格 
				printf("%d ",v[i][j]);
			}else{
				printf("%d",v[i][j]);
			}
		}
		cout << endl; 
	}
	
	return 0;
}
/*
一共n 块积木 编号1~n
一开始 第i 块积木放置在 i位置上
然后操作 m 次 输入a,b  吧b 位置上的积木全部放在 a 位置上

输入: 
4 4
3 1
4 3
2 4
2 2
输出: 
2 4 3 1 


*/ 
