#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> v[10005];

int main(){
	int n,m,a,b;
	scanf("%d %d",&n,&m);
	for(int i=1;i<=n;i++){  // ��Ŵ�1 ��ʼ 
		v[i].push_back(i);
	}
	
	for(int i=0;i<m;i++){
		scanf("%d %d",&a,&b);
		if(a == b){  // �Լ������Լ��ͺ��鷳 ����Ҳ����Ҫ���� 
			continue;
		}
		for(int j=0; j<v[b].size(); j++){
			v[a].push_back(v[b][j]);
		}
		vector<int>().swap(v[b]);// ���һ��b ���ڴ� 
	}
	for(int i=1;i<n;i++){
		for(int j=0;j<v[i].size();j++){
			if(j!=v[i].size()){  // ���ƽ�β�Ŀո� 
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
һ��n ���ľ ���1~n
һ��ʼ ��i ���ľ������ iλ����
Ȼ����� m �� ����a,b  ��b λ���ϵĻ�ľȫ������ a λ����

����: 
4 4
3 1
4 3
2 4
2 2
���: 
2 4 3 1 


*/ 
