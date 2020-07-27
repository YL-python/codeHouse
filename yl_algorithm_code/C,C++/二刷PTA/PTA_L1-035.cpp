#include <iostream>
#include <cstring>
using namespace std;

int cnt=-1,flag=1,vis=0;
string s[20];

int main() {
	while(flag) {
		cnt++;
		cin >> s[cnt];
		if(s[cnt].length() == 1 && s[cnt][0] == '.') {
			break;
		}
		if(cnt == 1) {
			cout << s[cnt];
			vis++;
		}
		if(cnt == 13) {
			cout << " and " << s[cnt];
			vis++;
			break;
		}
	}
	if(vis==0) {
		cout << "Momo... No one is for you ...";
	} else if(vis == 1) {
		cout << " is the only one for you...";
	} else {
		cout << " are inviting you to dinner...";
	}

	return 0;
}
