# Time:- O(n)
# Space :- O(n)    
class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        self.maxval=0
        @lru_cache(maxsize=None)
        def maxp(lower):
            if lower==len(arr):
                return 0
            maxval=maxele=0
            for i in range(lower,min(len(arr),lower+k)):
                maxele=max(maxele,arr[i])
                maxval=max(maxval,maxele*(i-lower+1)+maxp(i+1))
            return maxval
        return maxp(0)
        
