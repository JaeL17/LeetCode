from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs_stack(visited, grid, position):
            row, col = position[0], position[1]
            visited[row][col] = True
            stack=deque()
            stack.append(position)
            while stack:
                row_, col_ = stack.pop()
                for move in directions:
                    row_new = row_ + move[0]
                    col_new = col_ + move[1]
                    if 0<=row_new<rows and 0<=col_new<cols:
                        if not visited[row_new][col_new] and grid[row_new][col_new] =='1':
                            stack.append((row_new,col_new))
                            visited[row_new][col_new] = True
        def bfs(visited, grid, position):
            queue = deque()
            queue.append(position)
            visited[position[0]][position[1]]=True
            while queue:
                row, col = queue.popleft()
                for row_, col_ in directions:
                    new_row = row+ row_
                    new_col = col + col_
                    if 0<=new_row<rows and 0<= new_col< cols:
                        if not visited[new_row][new_col] and grid[new_row][new_col] =='1':
                            queue.append((new_row,new_col))
                            visited[new_row][new_col] =True

        def dfs_recursive(visited,grid, position):
            visited[position[0]][position[1]]=True
            for row_, col_ in directions:
                row_new = position[0]+row_
                col_new = position[1]+col_
                if 0<=row_new<rows and 0<=col_new<cols:
                    if not visited[row_new][col_new] and grid[row_new][col_new] =='1':
                        dfs_recursive(visited,grid,(row_new,col_new))

        directions = [(1,0), (-1,0), (0,1), (0,-1)] # up, down, right, left
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] =='1':
                    count +=1
                    dfs_stack(visited, grid, (row,col))
        return count    

