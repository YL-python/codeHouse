#include <iostream>
using namespace std;

int n,a[10005];
int ans=1;

int l(int x,int y){
	return a[x]-a[y]==1?1:0;
}

int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}

	for(int i=0;i<n;i++){
		for(int j=i+1;j<=n;j++){
			if(! l(j,j-1)){
				ans = ans > (j-i) ? ans: j-i;
				break;
			}else{
				ans = ans > (j-i) ? ans: j-i;
			}
		}
		
	}
	cout << ans;
	return 0;
}
