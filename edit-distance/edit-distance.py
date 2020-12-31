class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None)
        def mcs(i,j):
            if i==len(word1) and j==len(word2):
                return 0
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if word1[i]==word2[j]:
                return mcs(i+1,j+1)
            insert=1+mcs(i+1,j)
            delete=1+mcs(i,j+1)
            replace=1+mcs(i+1,j+1)
            return min(insert,delete,replace)
        return mcs(0,0)
        
