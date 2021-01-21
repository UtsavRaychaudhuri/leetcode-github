class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i=0
        k=len(matrix)-1
        j=0
        l=len(matrix[0])-1
        res=[]
        while(i<=k and j<=l):
            for a in range(j,l+1):
                res.append(matrix[i][a])
            i+=1
            if i>k or j>l:
                break
            for a in range(i,k+1):
                res.append(matrix[a][l])
            l-=1
            if i>k or j>l:
                break
            for a in range(l,j-1,-1):
                res.append(matrix[k][a])
            k-=1
            if i>k or j>l:
                break
            for a in range(k,i-1,-1):
                res.append(matrix[a][j])
            j+=1
        return res
            
                
                
            
                
