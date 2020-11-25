class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        res=-sys.maxsize
        while(i<j):
            res=max(res,min(nums[i],nums[j])*(j-i))
            if nums[i]<nums[j]:
                i+=1
            else:
                j-=1
        return res
