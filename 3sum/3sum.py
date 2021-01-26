class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        limit=nums[0]
        res=[]
        i=0
        while(i<len(nums) and nums[i]<=abs(nums[0])):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            k=i+1
            j=len(nums)-1
            while(k<j):
                if nums[k]+nums[j]>abs(nums[i]):
                    j-=1
                elif nums[k]+nums[j]<abs(nums[i]):
                    k+=1
                else:
                    res.append([nums[i],nums[k],nums[j]])
                    k+=1
                    j-=1
                    while k < j and nums[k]==nums[k-1] and nums[j]==nums[j+1]:
                        k += 1
                        j-=1
            i+=1
        return res
