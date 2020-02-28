#include <iostream>
using namespace std;
char num[1005][20];
int sj[1005],ks[1005];
int vis[1005];
int m,n;
int main (){
	cin >> n;
	for(int i=0;i<n;i++){
		cin>>num[i];
		cin>>sj[i]>>ks[i];
//		scanf("%s",&num[i]);
//		scanf("%d%d",&sj[i],&ks[i]);
	}
//	scanf("%d",&m);
	cin>>m;
	for(int i=0;i<m;i++){
		cin>>vis[i];
//		scanf("%d",&vis[i]);
	}
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			if(vis[i]==sj[j]){
				cout<<num[j]<<" "<<ks[j]<<endl;
//				printf("%s %d\n",num[j],ks[j]);
			}	
		}
	}
	return 0;
} 
