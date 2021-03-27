class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j=0
        my_map={}
        res=0
        i=0
        while i<len(s):
            if s[i] in my_map and my_map[s[i]]>=j:
                res=max(res,i-j)
                j=my_map[s[i]]+1
                my_map[s[i]]=i
            else:
                my_map[s[i]]=i
            i+=1
        return max(res,i-j)
    
            
                
                