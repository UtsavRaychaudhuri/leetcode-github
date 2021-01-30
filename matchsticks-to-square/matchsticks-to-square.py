class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        visited=[False]*len(nums)
        nums.sort(reverse=True)
        if sum(nums)%4>0:
            return False
        eachside=sum(nums)//4
        @lru_cache(maxsize=None)
        def ms(side,eachside):
            if eachside==0:
                side+=1
            if side==4 and eachside==0:
                return True
            if eachside==0:
                eachside=sum(nums)//4
            if eachside<0:
                return False
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i]=True
                    eachside-=nums[i]
                    if ms(side,eachside):
                        return True
                    eachside+=nums[i]
                    visited[i]=False
        return ms(0,eachside)
        
                    