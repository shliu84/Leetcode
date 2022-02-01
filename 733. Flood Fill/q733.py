#https://youtu.be/0ONI1_C3XnU
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs (image, r, c, color, newColor, arr):

            if image[r][c] == color and arr[r][c] == 0:
                image[r][c] = newColor
                arr[r][c] = 1
                if r > 0: 
                    dfs(image, r-1,c,color,newColor, arr)
                if r < len(image)-1: 
                    dfs(image, r+1,c,color,newColor, arr)
                if c > 0: 
                    dfs(image, r,c-1,color,newColor, arr)
                if c < len(image[0])-1: 
                    dfs(image, r,c+1,color,newColor, arr)

        arr = [ [0]*len(image[0]) for i in range(len(image))]
        if image[sr][sc] != newColor:
            dfs(image, sr,sc, image[sr][sc],newColor, arr)
        return image