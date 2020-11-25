class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini=maxi=nums[0]
        global_max=maxi
        for i in range(1,len(nums)):
            mini,maxi=min(nums[i],mini*nums[i],maxi*nums[i]),max(nums[i],mini*nums[i],maxi*nums[i])
            global_max=max(maxi,global_max)
        return global_max
            
