#include <iostream>
#include <string>
#include <map> 
#include <cstdio>
using namespace std;

int main(){
	int n;
	map<string,int> mp;
	// string s;
	char s[20];
	cin >> n;
	for(int i=0;i<n;i++){
		// cin >> s;
		scanf("%s",s);
		mp[s]++;
	}
	
	// out << mp.size() << endl;
	printf("%d\n",mp.size()); 
	
	for(map<string, int>::iterator i=mp.begin(); i!=mp.end(); i++){
		// cout << i->first << " " << i->second << endl;
		printf("%s %d",(i->first).c_str(),i->second);
	}
	
	return 0;
}
/*
输入书名
输出每本书的数量 
*/  
