class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res=[]
        def check(query,pattern):
            j=0
            for i in range(len(query)):
                if query[i].isupper():
                    if j<len(pattern) and pattern[j]==query[i]:
                        j+=1
                    else:
                        return False
                elif j<len(pattern) and query[i]==pattern[j]:
                    j+=1
            if j<len(pattern):
                return False
            return True             
        for query in queries:
            res.append(check(query,pattern))
        return res