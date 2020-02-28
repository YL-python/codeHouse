#include <iostream>
#include <string>

using namespace std;
int n,m;
char s[105][105];
int dir[8][2] = {{-2,-1},{-2,1},{2,-1},{2,1},{1,2},{1,-2},{-1,2},{-1,-2}};

void dfs(int x, int y, int step){
	if(step>3){
		return ;
	}
	if(x<0 || x>=n || y<0 || y>=m){
		// 不能判断重复，因为重复的可能走的步数不一样 
		return ;
	}
	
	s[x][y] = '#';
	for(int i=0;i<8;i++){
		dfs(x+dir[i][0], y+dir[i][1], step + 1);
		// step++  和  ++ step 在for循环内会变值 
	}	
}

int main(){
	int x,y; 
	scanf("%d%d%d%d",&n,&m,&x,&y);
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			s[i][j] = '.';
		}
	}
	dfs(x-1, y-1, 0);
	
	for(int i=0;i<n;i++){
		printf("%s\n",s[i]);
	}
	return 0;
}
/*
他想知道这个马走三步之内可以到达的位置，是否;
有好的对策可以给大师致命一击。现在蒜头君的脑
子已经不足以想出马走三步之内能到达的所有位瞥
了。于是他找到作为他好朋友的你来帮忙解决这个
问题，

10 9 
10 1

.........
.........
.........
.#.#.....
#.#.#....
####.#...
#####.#..
##.###...
#.###.#..
######...
*/ 



























