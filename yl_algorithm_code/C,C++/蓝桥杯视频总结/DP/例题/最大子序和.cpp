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
����һ���������� nums���ҵ�һ���������͵����������飨���������ٰ���һ��Ԫ�أ������������͡�

ʾ��:

����: [-2,1,-3,4,-1,2,1,-5,4],
���: 6
����:���������� [4,-1,2,1] �ĺ����Ϊ6��

dp[i] = max(dp[i-1]+nums[i], nums[i])

*/ 
