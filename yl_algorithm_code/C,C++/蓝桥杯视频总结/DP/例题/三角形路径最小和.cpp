class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if(triangle.size() == 0){
            return 0;
        }
        vector<vector<int> > dp(triangle);
        for(int i=triangle.size()-2;i>=0;i--) {        
            for(int j=0; j<triangle[i].size(); j++) {
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j];
            }
        }
        return dp[0][0];
    }
};
/*
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

自顶向下，考虑边界条件要特殊处理 , minPath[i][j] = Min()minPath[i-1][j-1], minPath[i-1][j]) + a[i][j], 
动态规划, 自底向上  递推式 dp[i][j] = min(dp[i+1][j], dp[i+1[j+1]) + triangle[i][j];
*/ 
