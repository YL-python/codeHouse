#include<iostream>
#include<algorithm>
using namespace std;

long long n,q,a[1000005],ans;

int main() {

	cin >> n >> q;
	for(long long i=1; i<=n; i++) {
		cin >> a[i];
	}

	if(n == 0) {
		cout << 0;
		return 0;
	}

	long long i=1, j=n;
	while(i<j) {
		if(a[i] < a[j]) {
			ans += a[i] * q;
//			printf("吃了%d  现在ans 是 ：%d \n",a[i],ans);
			i++;
		} else {
			ans += a[j] * q;
//			printf("吃了%d  现在ans 是 ：%d \n",a[j],ans);
			j--;
		}
		q++;
	}
	ans += a[i] * q;
//	printf("吃了%d  现在ans 是 ：%d \n",a[i],ans);
	cout << ans;
	return 0;
}

