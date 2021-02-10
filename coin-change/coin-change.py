class Solution:
    def coinChange(self, nums: List[int], amount: int) -> int:
        self.res=sys.maxsize
        @lru_cache(maxsize=None)
        def cc(amt,i):
            if amt==amount:
                return 0
            if amt>amount or i==len(nums):
                return sys.maxsize    
            return min(1+cc(amt+nums[i],i),cc(amt,i+1))
        ans=cc(0,0)
        if ans==sys.maxsize:
            return -1
        return ans