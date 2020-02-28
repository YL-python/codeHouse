class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int dp = nums[0];
        int ans = nums[0];
        for(int i=1;i<nums.size();i++){
            dp = max(dp+nums[i],nums[i]);
            if(ans < dp){
                ans = dp;
            }
        }
        return ans;
    }
};
/*
给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释:连续子数组 [4,-1,2,1] 的和最大，为6。

dp[i] = max(dp[i-1]+nums[i], nums[i])

*/ 
