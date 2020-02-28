#include <iostream>
#include <queue>

using namespace std;

void bfs(起始点){
	把起始点放入队列
	标记起始点访问
	while( 队列不为空 ){
		访问队首元素 x
		删除队首元素
		for(x 所有相邻点 ){
			if(该点没有访问且合法){
				把该点加入到队列末尾 
			} 
		} 
	}
	队列为空，广搜结束 
} 

int main(){
	
	return 0;
}




























