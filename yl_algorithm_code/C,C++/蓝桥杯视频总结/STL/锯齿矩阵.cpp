#include <iostream>
#include <string>
#include <vector> 
using namespace std;

// ����һά���鳤��10005  ÿһ��װһ����̬���� 
// ��ʵ���Ƕ�ά��̬����  ֻ������һά��Сȷ���� 
// ����д����  vector �ĵײ�ʵ��ԭ�� 
vector<int> a[10005]; 
int n,m; 
/* 
һ������n�� m��Ԫ�� ÿһ�е�Ԫ�ض�����ͬ�о�ݾ��� 
1 12 2 2
1 2 3
4 7 0 8 11 
ÿһ�еĳ��Ȳ��̶���vertor��װ 
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

