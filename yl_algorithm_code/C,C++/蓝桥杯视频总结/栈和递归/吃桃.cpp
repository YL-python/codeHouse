#include <iostream>
#include <string>

using namespace std;

int n;

int f(int x){
	if(x == n){
		return 1;
	}else{
		return (f(x + 1) + 1) * 2;
	}
}

int main(){
	
	scanf("%d",&n);
	printf("%d\n",f(1)); 
	
	return 0;
}
/*
蒜头君买了一堆桃子不知道个数，第 1 天吃了一半.
的桃子，还不过瘾，又多吃了一个。以后他每天吃
剩下的桃子的 1半 还多一个，到 n 天只剩下一个桃
子了。蒜头君想知道 1 开始买了多少桃子。
*/ 



























