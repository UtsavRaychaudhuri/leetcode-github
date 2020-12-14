class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList or endWord not in wordList:
            return 0
        q=collections.deque([])
        q.append(beginWord)
        s="abcdefghijklmnopqrstuvwxyz"
        my_set=set()
        visited=set()
        for i in wordList:
            my_set.add(i)
        res=1
        visited.add(beginWord)
        while(q):
            size=len(q)
            for i in range(size):
                word=q.popleft()
                for i in range(len(word)):
                    for j in s:
                        newword=word[:i]+j+word[i+1:]
                        if newword in my_set and newword not in visited:
                            if newword==endWord:
                                return res+1
                            q.append(newword)
                            visited.add(newword)
            res+=1
