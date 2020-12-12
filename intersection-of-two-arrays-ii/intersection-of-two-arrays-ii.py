class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums1)<len(nums2):
            s,h=nums1,nums2
        else:
            s,h=nums2,nums1
        def bs(arr,i,target):
            l=i
            h=len(arr)-1
            while(l<h):
                mid=(l+h)>>1
                if arr[mid]==target:
                    h=mid
                elif arr[mid]>target:
                    h=mid-1
                else:
                    l=mid+1
            return l
        res=[]
        idx=0
        for i in range(len(s)):
            idx=bs(h,idx,s[i])
            if idx<len(h):
                if h[idx]==s[i]:
                    res.append(s[i])
                    idx+=1
        return res
        
