#include <stdio.h>

int n,m,pep[100005],cnt;

int main() {

	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&m);  // m ������
		for(int j=0; j<m; j++) {
			scanf("%d",&cnt);  // ��ǰ����
			if(m!=1) { // ֻ��һ���˵�ʱ����û������Ȧ��
				pep[cnt] = 1;  // �����������Ϊ������Ȧ
			}
		}
	}
	scanf("%d",&m);  // Ҫ��������
	int flag = 0;
	for(int i=0; i<m; i++) {
		scanf("%d",&cnt);  // ��ǰ���ĺ���
		if(pep[cnt] == 0) {  // �����û������Ȧ
			if(flag!=0) {  // ��ֹ��һ�� �ո�
				printf(" ");
			}
			printf("%05d",cnt);
			pep[cnt] = 1; // ��ֹһ���˱�������
			flag++;
		}
	}
	if(flag==0)  {
		printf("No one is handsome");
	}
	return 0;
}
