class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        board2 = copy.deepcopy(board)
        
        
        
        def bfs(matrix,row,col):
            countOfNeighbors = 0
            directions = [[-1,1],[-1,-1],[1,1],[1,-1],[1,0],[-1,0],[0,1],[0,-1]]
            
            for dx,dy in directions:
                vx,vy = dx + row, dy + col
                
                if vx < 0 or vy < 0 or vx >= len(matrix) or vy >=len(matrix[0]):
                    continue
                
                if matrix[vx][vy] == 1:
                    countOfNeighbors += 1
            return countOfNeighbors 
        

        
        for row in range(len(board2)):
            for col in range(len(board2[0])):
                neighbors = bfs(board2,row,col)
                if board2[row][col] == 1 and neighbors < 2:
                    board[row][col] = 0 
                    
                elif board2[row][col] == 1 and (neighbors == 2 or neighbors == 3):
                    board[row][col] = 1
                    
                elif board2[row][col] == 1 and neighbors > 3:
                    
                    board[row][col] = 0 
                    
                elif board2[row][col] == 0 and neighbors == 3:
                    board[row][col] = 1
                    
            
                    
            
        