class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination=len(nums)-1
        for i in range(destination-1,-1,-1):
            if i+nums[i]>=destination:
                destination=i
        return destination==0
        # # DFS:- TLE
        # def canreach(index):
        #     if index>=len(nums)-1:
        #         return True
        #     for i in range(1,nums[index]+1):
        #         if canreach(index+i):
        #             return True
        #     return False
        # return canreach(0)
            
            
