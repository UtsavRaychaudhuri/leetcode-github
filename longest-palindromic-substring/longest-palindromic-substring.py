class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlength=0
        self.string=""
        if len(s)==1:
            return s
        def checkpalindrome(i,j):
            while(i>=0 and j<len(s) and s[i]==s[j]):
                i-=1
                j+=1
            if j-i-1>maxlength:
                self.string=s[i+1:j]
            return j-i-1
        for i in range(len(s)-1):
            maxlength=max(maxlength,checkpalindrome(i,i),checkpalindrome(i,i+1))
        return self.string
        