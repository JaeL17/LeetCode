from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        fresh_oranges: dict[str, List[int]] = dict()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

        def bfs(pos_min: Tuple[int, int, int]) -> None:
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            queue : List[Tuple[int, int, int]] = deque([pos_min])
            visited[pos_min[0]][pos_min[1]] = True

            while queue:
                curr_r, curr_c, curr_t = queue.popleft()   
                for move in moves:
                    new_r, new_c = curr_r + move[0], curr_c + move[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if grid[new_r][new_c] == 1 and not visited[new_r][new_c]: # check for fresh orange
                            fresh_oranges[f"{new_r}_{new_c}"].append(curr_t)
                            queue.append((new_r, new_c, curr_t + 1))
                            visited[new_r][new_c] = True

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges[f"{row}_{col}"] = []

        if len(fresh_oranges) == 0: # check whether there is no fresh orange 
            return 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    bfs((row, col, 1))

        answer = []
        for key, val in fresh_oranges.items():
            if not val:
                return -1
            else:
                answer.append(min(val))
            
        return max(answer) #if answer else -1


        