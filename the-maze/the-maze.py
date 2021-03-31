class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start==destination:
            return True
        q=collections.deque([])
        q.append(start)
        dirs=[[0,1],[-1,0],[0,-1],[1,0]]
        while(q):
            ele=q.popleft()
            if ele==destination:
                return True
            for i,j in dirs:
                k,l=ele[0]+i,ele[1]+j
                while(k>=0 and k<len(maze) and l>=0 and l<len(maze[0]) and maze[k][l]!=1):
                    k+=i
                    l+=j
                k-=i
                l-=j
                if maze[k][l]!=2:
                    q.append([k,l])
                    maze[k][l]=2
        return False
                
                    
                    
                
                
            