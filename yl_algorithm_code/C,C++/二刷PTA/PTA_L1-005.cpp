#include<iostream>
#include<string>
using namespace std;

/* ����˵��
str: ����ĸ�����Ϣ�� sj��������Ի����룬zk�������׼����λ���� 
n,m��Ŀ�ģ�cnt������m������� ��ѯ �Ի�����

����һ�����ݽṹ����˵һ���ɵķ����� 
strList���±��� �Ի����룬ֵ�� ��Ӧ�˵����֤�� 
vis�� �±��� �Ի����룬ֵ�� ��Ӧ�˵�׼����λ���� 

˼·�ܶ� ���Դ浽�������������Ȼ��if�ж����
��������д�����������ռ�׬ȡʱ��� 
*/
string strList[1005],str;
int vis[1005];
int n,m,cnt,sj,zk;

int main() {
	cin >> n;
	while(n--){
		cin >> str >> sj >> zk;
		strList[sj] = str;
		vis[sj] = zk;
	}
	cin >> m;
	while(m--){
		cin >> cnt;
		cout << strList[cnt] << " " << vis[cnt] << endl;
	}
	return 0;
}
