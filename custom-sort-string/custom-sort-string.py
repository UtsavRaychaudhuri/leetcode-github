class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c=collections.Counter(T)
        res=[]
        for i in S:
            if i in c:
                res.extend([i]*c[i])
                del c[i]
        for i in c:
            res.extend([i]*c[i])
        return "".join(res) 
    