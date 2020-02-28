#include <iostream>
#include <string>
using namespace std;

/*
其实位置在原点向，x轴正方向
 多次输入方向和步数
 输出最终的位置
 
*/

int dx[4] = {0,-1,0,1};  //上 左 下 右 
int dy[4] = {1,0,-1,0}; 
char op[105];
int n,  // 输入步数 
	d=3,  // 记录方向，开始向右，就是3 
	count,  // 每一次走的步数 
	nowx=0,  // 当前位置 
	nowy=0;  // 当前位置 
	
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		if(op[0] == 'l'){ // left 左走 右的左边是 上就加 1
			d = (d + 1) % 4; 
		}else if(op[0] == 'r'){  // right 右走  右的右边是 下就加 3  
			d = (d + 3) % 4; 
		}else (op[0] == 'b'){  // break 后   右的后边是 左就加 2 
			d = (d + 2) % 4; 
		}  // 向前走不用管
		nowx = dx[d] * count;
		nowy = dy[d] * count;
	}
	cout<< nowx << " " << nowy;
	return 0;
}

