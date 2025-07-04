class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(y, x):
            if y < 0 or x < 0 or \
               y >= len(grid) or x >= len(grid[0]) or \
               grid[y][x] == 0:
                return 1
            if (y, x) in visit:
                return 0
            
            count = 0
            visit.add((y, x))
            count += dfs(y, x + 1)
            count += dfs(y + 1, x)
            count += dfs(y, x - 1)
            count += dfs(y - 1, x)
            return count
                
        # Find land to start from
        for y in range (len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    return dfs(y, x)