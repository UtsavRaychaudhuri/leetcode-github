class Solution:
    def customSortString(self, S: str, T: str) -> str:
        t=collections.Counter(T)
        res=[]
        for i in S:
            if i in t:
                res.append(i*t[i])
                del t[i]
        for i in t:
            res.append(i*t[i])
        return "".join(res)
