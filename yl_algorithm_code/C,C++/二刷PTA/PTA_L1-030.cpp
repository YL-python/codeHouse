#include<iostream>
using namespace std;

struct stu {
	int sex, vis;//性别、访问标识
	string name;//姓名
};

int main() {
	stu s[51];
	int n;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> s[i].sex >> s[i].name;
		s[i].vis = 0;
	}

	for(int i=0; i<n/2; i++) {
		cout << s[i].name << " ";
		s[i].vis = 1;
		for(int j=n-1; j>=0; j--) {
			if(s[j].vis!=1 && s[j].sex != s[i].sex) {
				cout << s[j].name << endl;
				s[j].vis = 1;
				break;
			}
		}
	}


	return 0;
}
