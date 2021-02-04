class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        def backtrack(temp,sum,index):
            if sum==target:
                self.res.append(temp.copy())
                return
            if sum>target:
                return
            for i in range(index,len(candidates)):
                temp.append(candidates[i])
                backtrack(temp,sum+candidates[i],i)
                temp.pop()
        backtrack([],0,0)
        return self.res