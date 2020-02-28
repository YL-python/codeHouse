class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        if(dungeon.size() == 0){
            return 0;
        }
        // dp[i][j] 表示在 (i, j) 点需要的最小血量
        // dungeon[i][j] 表示在 (i, j) 点会变化的血量
        int row = dungeon.size();
        int colum = dungeon[0].size();
        vector<vector<int> >dp(row,vector<int>(colum, 0));
        dp[row- 1][colum-1] = max(1-dungeon[row- 1][colum-1], 1);
        for(int i=row-1;i>=0;i--){
            for(int j=colum-1;j>=0;j--){
                if(i==row-1 && j==colum-1){
                    continue;
                }else if(i==row-1){
                    // 上一个点走过来需要的最小血量 和当前点会变化的血量比较
                    dp[i][j] = max(1,dp[i][j+1]-dungeon[i][j]);
                }else if(j==colum-1){
                    dp[i][j] = max(1,dp[i+1][j]-dungeon[i][j]);
                }else{
                    // 找最小血量 的走
                    // 上一个点走过来需要的最小血量 和当前点会变化的血量比较
                    int temp = min(dp[i][j+1],dp[i+1][j]);  // 找最小血量
                    dp[i][j] = max(1, temp-dungeon[i][j]); // 和变化进行比较
                }
            }
        }
        return dp[0][0];
    }
};
/*

一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由?M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

?

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

自下向上思考
 上一步需要的最小血量 和当前点会变化的血量比较
  
*/ 
