class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    k,l=i+1,j+1
                    flag=True
                    res=max(res,1)
                    while(k<len(matrix) and l<len(matrix[0]) and matrix[k][l]=="1"):
                        for m in range(k,i-1,-1):
                            if matrix[m][l]!="1":
                                flag=False
                                break
                        if not flag:
                            break
                        for n in range(l,j-1,-1):
                            if matrix[k][n]!="1":
                                flag=False
                                break
                        if not flag:
                            break
                        else:
                            res=max(k-i+1,res)
                            k+=1
                            l+=1
        if res==0:
            return 0        
        return (res)**2               