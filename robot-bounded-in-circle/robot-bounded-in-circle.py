class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
              # N     E     S       W
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        k,l=0,0
        dir_now=0
        for i in instructions:
            if i=='G':
                k,l=k+dirs[dir_now][0],l+dirs[dir_now][1]
            elif i=='L':
                dir_now=(dir_now+1)%4
            elif i=='R':
                dir_now=(dir_now+3)%4
        if (k==0 and l==0) or (dir_now>0):
            return True
        return False
            
                
            
            
        
                