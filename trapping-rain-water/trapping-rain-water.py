# Time:- O(n)
# Space:- O(1)
# Approach:- 
class Solution(object):
    def trap(self, bars):
        """
        :type height: List[int]
        :rtype: int
        """
        lw,rw=0,len(bars)-1
        left,right=0,len(bars)-1
        res=0
        while left<=right:
            if lw==left:
                left+=1
                continue
            if rw==right:
                right-=1
                continue
            if bars[lw]<bars[left]:
                lw=left
                continue
            if bars[rw]<bars[right]:
                rw=right
                continue
            if bars[lw]<=bars[rw] and bars[left]<=bars[lw]:
                res+=bars[lw]-bars[left]
                left+=1
                continue
            elif bars[rw]<bars[lw] and bars[right]<bars[lw]:
                res+=bars[rw]-bars[right]
                right-=1
                continue
        return res
