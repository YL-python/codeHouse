#include <cstdio>

using namespace std;

bool ss_book[20005];
int n;

void make_ss() {
	ss_book[0] = ss_book[1] = true;
	for(int i=2; i<20005; i++) {
		for(int j=i*2; j<20005; j+=i) {
			ss_book[j] = true;
		}
	}
}

int main() {
	make_ss();
	scanf("%d",&n);

	if(!ss_book[n-4]) {
		printf("%d %d %d",2,2,n-4);
		return 0;
	}

	for(int i=3; i<=n; i+=2) {
		for(int j=i; j<=n; j+=2) {
			if(!ss_book[i]&&!ss_book[j]&&!ss_book[n-i-j]) {
				printf("%d %d %d",i,j,n-i-j);
				return 0;
			}
		}
	}

	return 0;
}
