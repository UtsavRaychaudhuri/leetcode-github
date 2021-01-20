class Solution:
    def exist(self, board, word):
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        def backtrack(i,j,index):
            if 0<=i<len(board) and 0<=j<len(board[0]) and index<len(word) and word[index]==board[i][j]:
                if index==len(word)-1:
                    return True
            else:
                return False
            tmp=board[i][j]
            board[i][j]=''
            for k,l in dirs:
                if backtrack(i+k,j+l,index+1):
                    return True
            board[i][j]=tmp
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0):
                        return True
        return False
