/*
用数组来模拟 栈
*/

#include <cstdio>

int s[10005];
// tot 是0  但是下标从1开始 ，习惯上用tot表示栈内元素个数
int tot=0;

void push(int x) {
	s[++tot] = x;
}

void pop() {
	tot--;
}

int  top() {
	return s[tot];
}

void print() {
	for(int i=1; i<=tot; i++) {
		printf("%d ",s[i]);
	}
	puts("");
}

int main() {
	push(1);
	print();
	printf("Top = %d \n",top());
	push(2);
	print();
	printf("Top = %d \n",top());
	push(3);
	print();
	printf("Top = %d \n",top());
	pop();
	print();
	printf("Top = %d \n",top());
	pop();
	print();
	printf("Top = %d \n",top());
	push(4);
	print();
	printf("Top = %d \n",top());
	push(5);
	print();
	printf("Top = %d \n",top());
	return 0;
}
