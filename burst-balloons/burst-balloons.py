class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)-1
        dp=[]
        for i in range(n):
            local=[]
            for j in range(n):
                local.append(0)
            dp.append(local)
        for p in range(1,n):
            for j in range(p, n):
                i = j-p
                dp[i][j] = max(
                    dp[i][k] + dp[k+1][j] + nums[i] * nums[k+1] * nums[j+1] \
                    for k in range(i,j)
                )
        
        return dp[0][n-1]
    
#     for (int k = left; k <= right; ++k)
# dp[left][right] = max(dp[left][right], nums[left-1] * nums[k] * nums[right+1] + dp[left][k-1] + dp[k+1][right])**
