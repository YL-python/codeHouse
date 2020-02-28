class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        vector<int> dp(nums.size(), 1);
        int lis = dp[0];
        for(int i=1; i< nums.size(); i++){
            for(int j=0; j<i; j++){
                if(nums[i] > nums[j] && dp[i] < dp[j] + 1){
                    dp[i] = dp[j] + 1;
                }
            }
            lis = lis < dp[i] ? dp[i] : lis;
        }
        return lis;
    }
};



/*
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是?[2,3,7,101]，它的长度是 4。



状态定义：dp[i] 表示第i 个数的最长上升子序列
dp[i] 的值和 dp[0] 到dp[i-1] 的值有关 最大值加一
只有 nums[i] > nums[j] 的情况下 dp[i] 才会是 dp[j] + 1
 
在用一个值求出 dp数组的最大值就行
 
*/
