#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

struct PAIR{
	string name;
	int fen;
};
bool cmp(PAIR a,PAIR b){
	if(a.fen != b.fen){
		return a.fen > b.fen;
	}else{
		int flag = strcmp(a.name.c_str(),b.name.c_str());
		if(flag > 0){
			return false;
		}else{
			return true;
		}
	}
}

int main() {
	vector<PAIR> pep;
	int n;
	string s;
	int num;
	cin >> n;
	for(int i=0;i<n;i++){
		PAIR p;
		cin >> p.name >> p.fen;
		pep.push_back(p);
	}
	sort(pep.begin(),pep.end(),cmp);
	for(int i=0;i<pep.size();i++){
		cout << pep[i].name << " " << pep[i].fen << endl;
	}
	
	return 0;
}
