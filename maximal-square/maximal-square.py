class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp=[]
        gm=0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=="1":
                    matrix[i][j]=min(int(matrix[i-1][j]),int(matrix[i-1][j-1]),int(matrix[i][j-1]))+1
                gm=max(gm,int(matrix[i][j]))
        if gm==0:
            for i in matrix:
                if "1" in i:
                    return 1
        return pow(gm,2)
                
            
