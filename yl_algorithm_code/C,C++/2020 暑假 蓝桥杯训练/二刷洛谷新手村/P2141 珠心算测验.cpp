#include <cstdio>

using namespace std;

int n,a[20005],ans;
int map[20005];
int vis[20005];

int main() {
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&a[i]);
		map[a[i]] = 1;
	}

	for(int i=0; i<n; i++) {
		for(int j=i+1; j<n; j++) {
			if(map[a[i] + a[j]] && vis[a[i] + a[j]] == 0) {
				ans++;
				vis[a[i] + a[j]] = 1;
			}
		}
	}
	printf("%d",ans);
	return 0;
}
