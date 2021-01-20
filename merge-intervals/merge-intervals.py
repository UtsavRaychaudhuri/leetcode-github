class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        intervals.sort()
        res=[intervals[0]]
        for i,j in intervals[1:]:
            if i<=res[-1][1]:
                res[-1][1]=max(res[-1][1],j)
            else:
                res.append([i,j])
        return res
            
