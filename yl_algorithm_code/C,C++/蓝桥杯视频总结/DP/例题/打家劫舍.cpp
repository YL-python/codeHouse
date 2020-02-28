class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        if(nums.size() == 1){
            return nums[0];
        }else if(nums.size() == 2){
            return std::max(nums[0],nums[1]);
        }else{
            std::vector<int> dp(nums.size(), 0);
            dp[0] = nums[0];
            dp[1] = max(nums[0],nums[1]);
            for(int i=2;i<nums.size();i++){
            	
                dp[i] = std::max(dp[i-2]+nums[i],dp[i-1]);
            }
            return dp[nums.size() - 1];
        }
    }
};
/*
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
偷窃到的最高金额 = 1 + 3 = 4 。

dp 方程 dp[i] = max(dp[i-2]+nums[i], dp[i-1])
*/
