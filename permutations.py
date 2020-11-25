class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack=[[]]
        out=[]
        for i in nums:
            l=len(stack)
            for j in stack[:l]:
                for k in range(len(j)+1):
                    if len(j)==len(nums)-1:
                        out.append(j[:k]+[i]+j[k:])
                    stack.append(j[:k]+[i]+j[k:])
        return out
