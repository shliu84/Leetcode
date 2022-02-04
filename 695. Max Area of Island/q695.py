class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs (image, i, j, arr):
            area = 0
            if image[i][j] == 1 and arr[i][j] == 0:
                area = 1
                arr[i][j] = 1
                if i > 0: 
                    area += dfs(image, i-1,j,arr)
                if i < len(image)-1: 
                    area += dfs(image, i+1,j,arr)
                if j > 0: 
                    area += dfs(image, i,j-1,arr)
                if j < len(image[0])-1: 
                    area += dfs(image, i,j+1,arr)
            return area

        arr = [ [0]*len(grid[0]) for i in range(len(grid))]
        maxArea = 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and arr[i][j] == 0:

                    maxArea = max(maxArea, dfs(grid, i, j, arr))
        return maxArea