class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # without sorting
        def intersection(nums1,d):
            res=[]
            for i in nums1:
                if i in d:
                    d[i]-=1
                    if d[i]==0:
                        del(d[i])
                    res.append(i)
            return res
                
            
        if len(nums1)>len(nums2):
            nums1=collections.Counter(nums1)
            return intersection(nums2,nums1)
        else:
            nums2=collections.Counter(nums2)
            return intersection(nums1,nums2)
        
        
