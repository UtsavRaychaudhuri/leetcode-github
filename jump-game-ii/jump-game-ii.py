class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<= 1:
            return 0
        l,r=0,nums[0]
        jumps=1
        while r<len(nums)-1:
            jumps+=1
            right=0
            for i in range(l,r+1):
                right=max(right,nums[i]+i)
            l,r=r,right
        return jumps
            
