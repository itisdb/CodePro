class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        visited, maxIsland = {}, 0
        def getIslandSize(row, col, size):
            visited[(row, col)] = size
            size[0]+=1
            for r, c in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0 <= row+r < len(grid) and 0 <= col+c < len(grid) and (row+r, col+c) not in visited and grid[row+r][col+c] == 1: 
                    getIslandSize(row+r, col+c, size)
        
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 1 and (row, col) not in visited: 
                    getIslandSize(row, col, [0])
                    maxIsland = max(maxIsland, visited[row, col][0])
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 0:
                    total, taken = 0, set()
                    for r, c in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if 0 <= row+r < len(grid) and 0 <= col+c < len(grid) and (row+r, col+c) in visited:
                            if id(visited[row+r, col+c]) not in taken: total+=visited[row+r, col+c][0]
                            taken.add(id(visited[row+r, col+c]))
                    ans = max(ans, total+1)
        return max(ans, maxIsland)