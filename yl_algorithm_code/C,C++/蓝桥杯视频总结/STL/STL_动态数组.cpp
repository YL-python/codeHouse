#include <iostream>
#include <string>
#include <vector>
using namespace std;

// vector��̬����  ��Ҫ vector ͷ�ļ�
// ���壺 vector<T> vec   ������������ T������Ϊvec�Ķ�̬����

int main() {
	vector<int> v;
	// push_back()  ��vector������������һ��Ԫ��
	v.push_back(0);
	v.push_back(1);
	v.push_back(2); // [1,2,3]

	// size()������ȡ��̬����ĳ���
	for(int i = 0; i < v.size(); i++) {
		cout << "v[" << i << "]=" << v[i] << endl;
	}
	cout << "------------------" << endl;

	// �޸�Ԫ�ؿ���ֱ�Ӹ�ֵ�����ܳ���
	v[0] = 2;
	v[1] = 1;
	v[2] = 0;
	for(int i = 0; i < v.size(); i++) {
		cout << "v[" << i << "]=" << v[i] << endl;
	}
	cout << "------------------" << endl;

	// pop_back() ɾ���������һ��Ԫ�صķ���
	v.pop_back();
	
	for(int i = 0; i < v.size(); i++) {
		cout << "v[" << i << "]=" << v[i] << endl;
	}
	cout << "------------------" << endl;

	// ֻ֧����β�����в��� Ϊ�˰�ʱ�临�Ӷȱ�� o(1)

	// ���
	// ����1 clear()����  ��������ݵ��ǲ�������ڴ�
	v.clear();
	// ����2 �½�һ��vector����ȥ�滻������
	vector<int>().swap(v);


	// ���캯��
	vector<int> v1(10,1); // ����������10 ��ֵȫΪ 1�Ķ�̬����	
	vector<int> v2(10);  // ����������10 ��ֵȫΪ 0�Ķ�̬����	
	
	
	// ��άvector����
	vector<vector<int> > vec2;  // �ո�Ҫд
	// vec2[0]; // ����д��Υ���� ��Ҫ�Ȱѵ�һά�ȳſ�  
	for(int i=0;i<3;i++){
		vector<int> x(i+1,1);  // �Ȱѵ�һά�ȳſ� 
		vec2.push_back(x);  // ��һά��װ��vec2���� 
	} 
	for(int i=0;i<3;i++){
		for(int j=0;j<=i;j++){
			cout << vec2[i][j] << " " ;
		}
		cout << endl;
	} 
	cout << "------------------" << endl;
	
	// ���� n�� m��Ϊ 0�Ķ�̬���� 
	vector<vector<int> > vec3(n, vector<int>(m, 0));
	 
	
	return 0;
}

























































