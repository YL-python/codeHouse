/*
��������ģ�� ջ
*/

#include <cstdio>

int s[10005];
// tot ��0  �����±��1��ʼ ��ϰ������tot��ʾջ��Ԫ�ظ���
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
