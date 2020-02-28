#include <iostream>
#include <string>
#include <set> 
using namespace std;

set<int> s;

int main(){
	 
	int n,m,temp,count=0;  // count ¿ØÖÆÐÐÄ©¿Õ¸ñ 
	scanf("%d%d",&n,&m);
	for(int i=0;i<n+m;i++){
		scanf("%d",&temp);
		s.insert(temp);
	}
	
	for(set<int>::iterator i=s.begin(); i != s.end(); i++){
		if(count != s.size()-1){
			printf("%d ",(*i));
		} else{
			printf("%d\n",(*i));
		}
	}
	
	return 0;
}

