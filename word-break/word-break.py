class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        @lru_cache(maxsize=None)
        def backtrack(s):
            if len(s)==0:
                return True
            for i in range(len(s)):
                if s[:i+1] in wordSet and backtrack(s[i+1:]):
                    return True
            return False
        return backtrack(s)
        
                