class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        size=max(nums)
        newnums=[0]*(size+1)
        for i in nums:
            newnums[i]+=i
        @lru_cache(maxsize=None)
        def hr(i):
            if i>=len(newnums):
                return 0
            return max(newnums[i]+hr(i+2),hr(i+1))
        return hr(0)
    