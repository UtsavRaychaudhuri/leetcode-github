class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        def backtrack(i,j,index,word):
            if 0<=i<len(board) and 0<=j<len(board[0]) and index<len(word) and board[i][j]==word[index] and not self.ret:
                if index==len(word)-1:
                    return True
            else:
                return
            tmp=board[i][j]
            board[i][j]=''
            if not self.ret:
                for k,l in dirs:
                    if backtrack(i+k,j+l,index+1,word):
                        self.ret=True
            board[i][j]=tmp     
        word_dict=collections.defaultdict(list)
        for i in range(len(words)):
            word_dict[words[i][0]].append(i)
        res=[]
        seen=set()
        self.ret=False  
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in word_dict:
                    for k in word_dict[board[i][j]]:
                        if words[k] not in seen:
                            if backtrack(i,j,0,words[k]) or self.ret:
                                self.ret=False
                                res.append(words[k])
                                seen.add(words[k])
        return res
                            
                    
