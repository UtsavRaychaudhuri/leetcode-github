class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def rob_bank(i):
            if i==len(nums)-1:
                return nums[i]
            if i>=len(nums):
                return 0
            return max(nums[i]+rob_bank(i+2),rob_bank(i+1))
        return rob_bank(0)
    
