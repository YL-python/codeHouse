#include <cstdio>

using namespace std;

int n,a1,b1,a2,b2,a3,b3,ans;

int main() {
	scanf("%d",&n);

	scanf("%d%d",&a1,&b1);
	scanf("%d%d",&a2,&b2);
	scanf("%d%d",&a3,&b3);

	int _a1=a1,_b1=b1;
	while(_a1 < n) {
		_a1+=a1;
		_b1+=b1;
	}
	ans = _b1;

	int _a2=a2,_b2=b2;
	while(_a2 < n) {
		_a2+=a2;
		_b2+=b2;
	}
	_b2>ans?_b2:ans=_b2;

	int _a3=a3,_b3=b3;
	while(_a3 < n) {
		_a3+=a3;
		_b3+=b3;
	}
	_b3>ans?_b3:ans=_b3;
	printf("%d",ans);
	return 0;
}
