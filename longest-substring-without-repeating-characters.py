class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {}
        
        start = max_length = 0
        
        for i in range(len(s)):
            if s[i] in dict and start <= dict[s[i]]:
                start = dict[s[i]]+1
            else:
                max_length = max(max_length, i-start+1)
            
            dict[s[i]] = i
        
        return max_length
