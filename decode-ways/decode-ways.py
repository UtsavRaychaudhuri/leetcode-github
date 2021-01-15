class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def dfs(s):
            if len(s)>0 and s[0]=='0':
                return 0
            if s=="" or len(s)==1:
                return 1
            if int(s[:2])<27:
                one=dfs(s[1:])
                two=dfs(s[2:])
                return one+two
            else:
                return dfs(s[1:])
        return dfs(s)
        
