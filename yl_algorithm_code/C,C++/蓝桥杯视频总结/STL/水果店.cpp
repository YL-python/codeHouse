#include <iostream>
#include <string>
#include <map> 
using namespace std;

map<string,map<string,int> > mp;

int main(){
	int n,x;
	string fruit,province;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> fruit >> province >> x;
		mp[province][fruit] += x;
	}
	
	for(map<string,map<string,int> >::iterator ip=mp.begin();ip!=mp.end();ip++){
		cout << ip->first <<endl;
		for(map<string,int>::iterator ifu=ip->second.begin();ifu!=ip->second.end();ifu++){
			cout << "   |---" << ifu -> first << "(" << ifu -> second << ")" << endl;
		}
	}
	
	
	return 0;
}
/*
����n������
ÿ�������� ˮ�����ƣ����۵����� ����
���� 
5
apple shangdong 3
pineapple guangzou 1
sugarcane guangzou 1
pineapple guangzou 3
pineapple guangzou 1

��� 
guangzou
   |---pineapple(5)
   |---sugarcane(1)
shangdong
   |---apple(3)
*/ 
