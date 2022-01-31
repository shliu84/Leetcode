#https://youtu.be/0ONI1_C3XnU
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs (image, r, c, color, newColor):
            
            if image[r][c] == color:
                image[r][c] = newColor
                if r > 0: 
                    dfs(image, r-1,c,color,newColor)
                if r < len(image)-1: 
                    dfs(image, r+1,c,color,newColor)
                if c > 0: 
                    dfs(image, r,c-1,color,newColor)
                if c < len(image[0])-1: 
                    dfs(image, r,c+1,color,newColor)
            
        if image[sr][sc] != newColor:
            dfs(image, sr,sc, image[sr][sc],newColor)
        return image