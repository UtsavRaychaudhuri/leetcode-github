class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs)==0:
            return 0
        @lru_cache(maxsize=None)
        def mc(i,j):
            if i==len(costs):
                return 0
            if j==0:
                return costs[i][j]+min(mc(i+1,1),mc(i+1,2))
            elif j==1:
                return costs[i][j]+min(mc(i+1,0),mc(i+1,2))
            else:
                return costs[i][j]+min(mc(i+1,0),mc(i+1,1))
        return min(mc(0,0),mc(0,1),mc(0,2))
            
        