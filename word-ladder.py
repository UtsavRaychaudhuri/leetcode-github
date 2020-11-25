class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        q=collections.deque([])
        q.append(beginWord)
        q.append(-1)
        s="abcdefghijklmnopqrstuvwxyz"
        res=1
        seen=set()
        while(q):
            ele=q.popleft()
            if ele in seen:
                continue
            if ele==-1:
                res+=1
                if len(q)==0:
                    return 0
                q.append(-1)
                continue
            seen.add(ele)
            for i in range(len(ele)):
                for j in s:
                    w=ele[:i]+j+ele[i+1:]
                    if w==endWord:
                        return res+1
                    if w in wordList and w not in seen:
                        q.append(w)
        return res
                        
                    
        
