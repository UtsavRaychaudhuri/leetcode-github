from collections import deque
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=deque()
        s=list(s)
        for i in range(len(s)):
            if s[i].isalpha():
                continue
            if s[i]==')':
                if len(a)>0:
                    if a[-1][0]=='(':
                        a.pop()
                    else:
                        a.append((s[i],i))
                else:
                    a.append((s[i],i))
            else:
                a.append((s[i],i))
        for i,j in a:
            s[j]=""
        return "".join(s)
                        
                
            
