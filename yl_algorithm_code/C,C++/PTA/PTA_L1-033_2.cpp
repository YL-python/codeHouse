#include<bits/stdc++.h>
using namespace std;

int main(){
	int y,n;
	cin >> y >> n;
	int age = -1;
	set<char> s;
	string str;
	
	while(s.size() != n){
		s.clear();
		str = to_string(y+ ++age);
		while(str.length())!=4){
			str = '0' + str; 
		}
		for(int i=0;i<4;i++){
			s.insert(str[i]);
		}
	}
	printf("%d %04d" , age,y+age);
	
	return 0;
}

