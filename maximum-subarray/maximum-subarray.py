class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        maxres=localres=nums[0]
        for i in range(1,len(nums)):
            localres=max(nums[i],nums[i]+localres)
            maxres=max(localres,maxres)
        return maxres
