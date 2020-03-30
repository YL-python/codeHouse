#include <iostream>
#include <vector>
#include <map>
using namespace std;

map<string,int> dict;
vector<string> ans;
string a;
int n,maxcnt=-1;

int main() {
	cin >> n >> a;
	for(int i=0; i<=a.length()-n; i++) {
		string temp;
		for(int j=0; j<n; j++) {
			temp = temp + a[i+j];
		}
		if(dict.count(temp)) {
			dict[temp] ++;
		} else {
			dict[temp] = 1;
		}
		if(dict[temp] > maxcnt) {
			maxcnt = dict[temp];
		}
	}
	if(maxcnt == 1) {
		cout << "NO"<< endl;
	} else {
		cout << maxcnt<< endl;
		for(int i=0; i<=a.length()-n; i++) {
			string temp;
			for(int j=0; j<n; j++) {
				temp = temp + a[i+j];
			}
			if(dict[temp] == maxcnt) {
				cout << temp<< endl;
				dict[temp] --;
			}
		}
	}
	return 0;
}
