class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_map={"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
        if digits=="":
            return []
        self.res=[]
        def backtrack(idx,local):
            if idx==len(digits):
                self.res.append("".join(local))
                return
            for i in digits_map[digits[idx]]:
                local.append(i)
                backtrack(idx+1,local)
                local.pop()
        backtrack(0,[])
        return self.res
                
            
