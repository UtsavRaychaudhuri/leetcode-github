class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def rightbs(low,hi):
            while(low<=hi):
                mid=(low+hi)>>1
                if nums[mid]==target:
                    if mid+1<=hi and nums[mid+1]==target:
                        low=mid+1
                    else:
                        return mid
                elif nums[mid]<target:
                    low=mid+1
                else:
                    hi=mid-1
            return low
        def leftbs(low,hi):
            while(low<=hi):
                mid=(low+hi)>>1
                if nums[mid]==target:
                    if mid-1>=low and nums[mid-1]==target:
                        hi=mid-1
                    else:
                        return mid
                    if nums[mid]<target:
                        low=mid+1
                    else:
                        hi=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    hi=mid-1
            return low
        left=leftbs(0,len(nums)-1)
        right=rightbs(0,len(nums)-1)
        if len(nums)>0 and 0<=left<len(nums) and 0<=right<len(nums) and nums[left]==target and right<len(nums) and nums[right]==target:
            return [left,right]
        return [-1,-1]
            
                
            