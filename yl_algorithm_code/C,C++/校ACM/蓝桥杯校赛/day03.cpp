#include <iostream>
#include <string>
using namespace std;
// �ڵ������ֵ = 2��n�η���һ

int n=10; 

int main(){
	int sum=1;
	for(int i=1;i<=n;i++){
		sum*=2;
	}
	printf("%d\n",sum-1);
	return 0;
}

