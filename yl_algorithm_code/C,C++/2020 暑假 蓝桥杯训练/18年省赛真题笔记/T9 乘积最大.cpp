#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long LL;

const LL MOD = 1000000009;
const int maxN = 100005;
int n,k;
vector<LL> pos,neg; // ���������͸������б�
LL ans,temp;

LL mul(vector<LL> a,int start,int end) {
	LL ans = 1;
	for(int i=start; i<=endl;) {
		ans = ans * a[i] % MOD;
	}
}

int main() {
	cin >> n>> k;
	for(int i=0; i<n; i++) {
		cin >> temp;  // �������������ж�
		if(temp > 0) pos.push_back(temp);
		if(temp < 0) neg.push_back(temp);
	}
	sort(pos.begin(),pos.end());
	sort(neg.begin(),neg.end());
	/*===��������===*/
	
	
	return 0;
}































