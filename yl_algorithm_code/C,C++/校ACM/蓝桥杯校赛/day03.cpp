#include <iostream>
#include <string>
using namespace std;
// 节点数最大值 = 2的n次方减一

int n=10; 

int main(){
	int sum=1;
	for(int i=1;i<=n;i++){
		sum*=2;
	}
	printf("%d\n",sum-1);
	return 0;
}

