class TrieNode:
    def __init__(self,letter):
        self.letter=letter
        self.children={}
        self.eow=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode("")
        self.longestword=""
        
    def dodfs(self):
        self.dfs(self.root,"")
        return self.longestword
        
    def insert(self,word):
        curr=self.root
        for i in word:
            if i not in curr.children:
                curr.children[i]=TrieNode(i)
            curr=curr.children[i]
        curr.eow=True
        
    def dfs(self,root,word):
        word+=root.letter
        if not root.eow and word!="":
            return
        if len(word)==len(self.longestword):
                self.longestword=min(word,self.longestword)
        if len(word)>len(self.longestword):
                self.longestword=word
        for i in root.children:
            self.dfs(root.children[i],word)
                
class Solution:
    def longestWord(self, words) -> str:
        node=Trie()
        for word in words:
            node.insert(word)
        return node.dodfs()