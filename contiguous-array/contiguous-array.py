class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap={0:-1}
        sumc=0
        res=0
        for i,v in enumerate(nums):
            if v==0:
                sumc-=1
            if v==1:
                sumc+=1
            if sumc in hashmap:
                res=max(res,i-hashmap[sumc])
            else:
                hashmap[sumc]=i
        return res
                
                