from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
#         ## dp based solution ##
#         dp = [float('inf')] * (n + 1)
#         dp[0] = 0  # base case
        
#         squares = [i*i for i in range(1, int(n**0.5) + 1)]
        
#         for i in range(1, n + 1):
#             for square in squares:
#                 if i < square:
#                     break
#                 dp[i] = min(dp[i], dp[i - square] + 1)
        
#         return dp[n]

        ## using queue and bfs ##
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        
        # Queue for BFS - (remaining sum, steps)
        queue = deque([(n, 0)])
        
        visited = set()
        
        while queue:
            remainder, steps = queue.popleft()
            for square in squares:
                next_val = remainder - square
                if next_val == 0:
                    return steps + 1
                if next_val < 0:
                    break
                if next_val not in visited:
                    visited.add(next_val)
                    queue.append((next_val, steps + 1))
