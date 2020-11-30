from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bs(left,right,x):
            while(left<right):
                mid=(left+right)//2
                if arr[mid]==x:
                    return mid
                if arr[mid]<x:
                    left=mid+1
                else:
                    right=mid-1
            return left-1
            
        left=bs(0,len(arr)-1,x)
        right=left+1
        res=collections.deque([])
        while(left>=0 and right<len(arr) and len(res)<k):
            if x-arr[left]<=arr[right]-x:
                res.appendleft(arr[left])
                left-=1
            else:
                res.append(arr[right])
                right+=1
        while(left>=0 and len(res)<k):
            res.appendleft(arr[left])
            left-=1
        while(right<len(arr) and len(res)<k):
            res.append(arr[right])
            right+=1
        return res
