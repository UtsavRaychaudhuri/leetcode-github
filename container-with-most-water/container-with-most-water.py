class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        res=0
        while(l<h):
            res=max(res,min(height[l],height[h])*(h-l))
            if height[l]>height[h]:
                h-=1
            elif height[l]<height[h]:
                l+=1
            else:
                l+=1
        return res