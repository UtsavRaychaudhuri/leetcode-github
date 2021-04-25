class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,hi=0,len(nums)-1
        while(low<=hi):
            mid=(low+hi)>>1
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    hi=mid-1
                else:
                    low=mid+1
            elif nums[mid]<target<=nums[hi]:
                low=mid+1
            else:
                hi=mid-1
        return -1
            
            
# [7,0,1,2,4,5,6]