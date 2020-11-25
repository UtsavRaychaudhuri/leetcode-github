class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.matchedparantheses=[]
        self.backtrack(n,n,"")
        return self.matchedparantheses
​
    def backtrack(self,open,close,stringgenerated):
        if close<open:
            return
        if open==close==0:
            self.matchedparantheses.append(stringgenerated)
            return
        if close<0 or open<0:
            return
        self.backtrack(open-1,close,stringgenerated+"(")
        self.backtrack(open,close-1,stringgenerated+")")
        
