class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        m, n, seen = len(maze), len(maze[0]), set()
        def dfs(i, j):
            if [i, j] == destination: return True
            for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
                x, y = i, j
                while 0 <= x+dx < m and 0 <= y+dy < n and not maze[x+dx][y+dy]:
                    x, y = x+dx, y+dy
                if (x,y) not in seen: 
                    seen.add((x,y))
                    if dfs(x,y): return True
            return False
        return dfs(*start)
