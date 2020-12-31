class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def mt(i,j):
            if j==len(triangle[i]):
                return sys.maxsize
            if i==len(triangle)-1:
                return triangle[i][j]
            return triangle[i][j]+min(mt(i+1,j),mt(i+1,j+1))
        return mt(0,0)
