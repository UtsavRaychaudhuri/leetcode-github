class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=nums[0]
        for j in range(1,len(nums)):
            i=i^nums[j]
        return i
        