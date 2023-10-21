class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])  
        directions = [[-1, 0], [0, -1]]       
        for row in range(len(grid)):          
            for col in range(len(grid[0])):
                tempList = []                 
                for direction in directions:  
                    dRow, dCol = direction[0], direction[1]  
                  
                    if 0 <= row + dRow <= rows - 1 and 0 <= col + dCol <= cols - 1: 
                      tempList.append(grid[row + dRow][col + dCol])  
                if len(tempList) == 1: 
                  grid[row][col] += tempList[0]  
                elif len(tempList) == 2: 
                  grid[row][col] += min(tempList) 
        return grid[-1][-1]
