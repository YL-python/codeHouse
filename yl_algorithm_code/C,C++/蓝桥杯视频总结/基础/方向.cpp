#include <iostream>
#include <string>
using namespace std;

/*
��ʵλ����ԭ����x��������
 ������뷽��Ͳ���
 ������յ�λ��
 
*/

int dx[4] = {0,-1,0,1};  //�� �� �� �� 
int dy[4] = {1,0,-1,0}; 
char op[105];
int n,  // ���벽�� 
	d=3,  // ��¼���򣬿�ʼ���ң�����3 
	count,  // ÿһ���ߵĲ��� 
	nowx=0,  // ��ǰλ�� 
	nowy=0;  // ��ǰλ�� 
	
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		if(op[0] == 'l'){ // left ���� �ҵ������ �Ͼͼ� 1
			d = (d + 1) % 4; 
		}else if(op[0] == 'r'){  // right ����  �ҵ��ұ��� �¾ͼ� 3  
			d = (d + 3) % 4; 
		}else (op[0] == 'b'){  // break ��   �ҵĺ���� ��ͼ� 2 
			d = (d + 2) % 4; 
		}  // ��ǰ�߲��ù�
		nowx = dx[d] * count;
		nowy = dy[d] * count;
	}
	cout<< nowx << " " << nowy;
	return 0;
}

