from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

        def bfs(pos: Tuple[int, int]):
            queue = deque([pos])

            while len(queue) > 0:
                curr_r, curr_c = queue.popleft()

                for move in moves:
                    new_r, new_c = curr_r + move[0], curr_c + move[1]
                    if 0<= new_r < rows and 0 <= new_c < cols:
                        if grid[new_r][new_c] =="1" and not visited[new_r][new_c]:
                            visited[new_r][new_c] = True
                            queue.append((new_r, new_c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    count +=1
                    visited[row][col] =True
                    bfs((row, col))
                    # dfs((row, col))





        return count 