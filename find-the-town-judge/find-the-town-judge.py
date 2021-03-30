class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and N==1:
            return 1
        trusts=[0]*(N+1)
        for i,j in trust:
            trusts[i]-=1
            trusts[j]+=1
        for i in range(len(trusts)):
            if trusts[i]==N-1:
                return i
        return -1