class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=collections.deque([])
        wordset=set(wordList)
        q.append(beginWord)
        seen=set()
        res=0
        if beginWord==endWord or endWord not in wordList:
            return 0
        res=0
        chars=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        while(q):
            res+=1
            size=len(q)
            for i in range(size):
                ele=q.popleft()
                if ele==endWord:
                    return res
                for i in range(len(ele)):
                    for j in chars:
                        newele = ele[:i]+j+ele[i+1:]
                        if newele in wordset:
                            q.append(newele)
                            wordset.remove(newele)
        return 0
                        
                        