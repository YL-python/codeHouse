#include <cstdio>

int a[100005],fnt,end;

#define push(x) s[++end]=x
#define pop() fnt++
#define size() end-fnt+1
#define front() s[fnt]

// �Լ���д���оͻ�����˷ѿռ������
// ��Ҫ���˷ѿռ����ѭ������
// ѭ���������±�ȥ % ����ĳ���
// queue���а�����ʵ����
