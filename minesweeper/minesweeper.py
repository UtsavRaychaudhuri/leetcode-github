class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs=[[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        q=collections.deque([])
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        q.append(click)
        seen=set()
        def checkmines(i,j):
            mines=0
            for k,l in dirs:
                m,n=i+k,j+l
                if 0<=m<len(board) and 0<=n<len(board[0]):
                    if board[m][n]=='M':
                        mines+=1
            if mines>0:
                board[i][j]=str(mines)
                return False
            return True
        while(q):
            k,l=q.popleft()
            board[k][l]='B'
            if checkmines(k,l):
                for i,j in dirs:
                    m,n=k+i,l+j
                    if 0<=m<len(board) and 0<=n<len(board[0]) and (m,n) not in seen:
                        board[m][n]='B'
                        q.append([m,n])
                        seen.add((m,n))
        return board
                
                    
                
                
