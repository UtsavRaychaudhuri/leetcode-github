class Solution:
    def countArrangement(self, n: int) -> int:
        self.res=0
        visited=[False]*(n+1)
        def backtrack(res,index):
            if len(res)>0:
                if res[-1]%len(res)>0 and len(res)%res[-1]>0:
                    return
            if index==n:
                self.res+=1
                return
            for i in range(1,n+1):
                res.append(i)
                if not visited[i]:
                    visited[i]=True
                    backtrack(res,index+1)
                    visited[i]=False
                res.pop()
        backtrack([],0)
        return self.res
