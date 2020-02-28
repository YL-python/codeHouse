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
			ans = i->first;  // map有按 key 排序的功能 
//			if(i->first > ans){
//				ans = i->first;
//			}
		}
	}
	
	cout << ans << " " << count << endl;
	
	return 0;
}
/*
输入n个数求最多出现的数和次数，次数重复时看值的最大值 
*/
