class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        my_set=set()
        for i in wordDict:
            my_set.add(i)
        wordnow=""
        dp=[0]
        for i in range(len(s)+1):
            for j in dp:
                if s[j:i] in my_set:
                    dp.append(i)
                    break
        if dp[-1]==len(s):
            return True
        return False
                
            
        
