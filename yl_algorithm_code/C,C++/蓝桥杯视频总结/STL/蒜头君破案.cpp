#include <iostream>
#include <string>
#include <set>
using namespace std;

struct pep{
	int h;
	int w;
	int age;
	pep(int _h, int _w, int _age){
		h = _h;
		w = _w;
		age = _age;
	}
	// operator<   ��ʾҪ���� < ��������  �Դ˶���������� 
	// (const �ṹ���� &������) const  �̶�д�� 
	bool operator<(const pep &rhs) const{
		if(h !=rhs.h){  // ��ʾ����h ��ͬ��ʱ�� ��������ʽ 
			return h < rhs.h;
		}
		if(w != rhs.w){
			return w < rhs.w;
		}
		return age < rhs.age;  // ��ʾ h��w����ͬ��ʱ���� age ������ 
	}
};

set<pep> s;

int main(){
	int n,m,h,w,age;
	cin >> n >> m;
	for(int i=0;i<n;i++){
		cin >> h >> w >> age;
		s.insert(pep(h,w,age));
	}
	for(int i=0;i<m;i++){
		cin >> h >> w >> age;
		if(s.count(pep(h,w,age))){  // ʱ�临�Ӷ���0(logn) �������Լ�����Ҫ�� 
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}
	}
	return 0;
}

/*
һ������ n����
��m���˵���Ϣ
������ m������
���� m��������û�п�����������е��� 

3 2
166 50 30
178 60 23
132 40 15
167 50 30
NO
178 60 23
YES
*/
