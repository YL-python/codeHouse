#include <string>
#include <iostream>
#include <map> 
using namespace std;

map<int,int> mp;

int main(){
	int n,x,ans=-1,count=-1;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> x;
		mp[x]++;
	} 
	
	for(map<int,int>::iterator i=mp.begin(); i!=mp.end();i++){
		if(i->second >= count){
			count = i->second;
			ans = i->first;  // map�а� key ����Ĺ��� 
//			if(i->first > ans){
//				ans = i->first;
//			}
		}
	}
	
	cout << ans << " " << count << endl;
	
	return 0;
}
/*
����n�����������ֵ����ʹ����������ظ�ʱ��ֵ�����ֵ 
*/
