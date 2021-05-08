class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ""
        res=[]
        def backtrack(openb,close,temp):
            if openb==0 and close==0:
                res.append("".join(temp))
                return
            if openb<0 or close<0:
                return
            if close<openb:
                return
            for i in ('(',')'):
                if i=='(':
                    openb-=1
                if i==')':
                    close-=1
                temp.append(i)
                backtrack(openb,close,temp)
                char=temp.pop()
                if char=='(':
                    openb+=1
                else:
                    close+=1
        backtrack(n,n,[])
        return res