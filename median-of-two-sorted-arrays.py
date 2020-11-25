class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = nums1 + nums2
        arr.sort()
        size = len(arr)
        half=size//2
        mod=size%2
        if mod==0:
            return ((arr[half]+arr[half-1])/2.0)
        return arr[half]/1.0
                
        
