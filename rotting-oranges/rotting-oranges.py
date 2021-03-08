class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        res=0
        fresh=0
        q=collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while(q):
            size=len(q)
            for i in range(size):
                k,l=q.popleft()
                for m,n in dirs:
                    if 0<=m+k<len(grid) and 0<=n+l<len(grid[0]) and grid[m+k][n+l]==1:
                        grid[m+k][n+l]=2
                        q.append([m+k,n+l])
                        fresh-=1
            res+=1
        if fresh==0:
            return res-1
        return -1
                        
                        
                        
                    