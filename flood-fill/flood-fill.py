class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        if image[sr][sc]==newColor:
            return image
        def dfs(i,j):
            temp=image[i][j]
            image[i][j]=newColor
            for k,l in dirs:
                if 0<=i+k<len(image) and 0<=j+l<len(image[0]) and image[i+k][j+l]==temp:
                    dfs(i+k,j+l)
        dfs(sr,sc)
        return image
                    