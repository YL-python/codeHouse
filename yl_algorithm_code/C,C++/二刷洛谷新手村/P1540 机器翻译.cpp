#include <cstdio>
#include <queue>
using namespace std;

int a[1005]= {0},n,m,temp,ans;
queue <int> q;

int main() {

	scanf("%d%d",&n,&m);
	while(m--) {
		scanf("%d",&temp);
		// ����ڴ�
		if(a[temp] == 0) {  // û��
			ans++;  // ��ѯ���� +1;
			a[temp] = 1;
			q.push(temp);
			if(n == 0) { // �ڴ�����
				int cnt = q.front();
				q.pop();
				a[cnt] = 0;
			} else {
				n--;
			}
		}
	}

	printf("%d",ans);

	return 0;
}
