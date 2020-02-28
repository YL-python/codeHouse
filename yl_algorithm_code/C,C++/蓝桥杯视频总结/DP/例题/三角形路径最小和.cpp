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
����һ�������Σ��ҳ��Զ����µ���С·���͡�ÿһ��ֻ���ƶ�����һ�������ڵĽ���ϡ�

���磬���������Σ�

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

�Զ����£����Ǳ߽�����Ҫ���⴦�� , minPath[i][j] = Min()minPath[i-1][j-1], minPath[i-1][j]) + a[i][j], 
��̬�滮, �Ե�����  ����ʽ dp[i][j] = min(dp[i+1][j], dp[i+1[j+1]) + triangle[i][j];
*/ 
