from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # --------------------------
        # Step 1: distance to nearest thief
        # --------------------------
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    dist[nr][nc] == -1
                ):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # --------------------------
        # Step 2: Can we reach end if
        # every cell must have dist >= limit?
        # --------------------------
        def can(limit):

            if dist[0][0] < limit:
                return False

            q = deque([(0,0)])
            visited = [[False]*n for _ in range(n)]
            visited[0][0] = True

            while q:

                r, c = q.popleft()

                if r == n-1 and c == n-1:
                    return True

                for dr, dc in directions:

                    nr, nc = r+dr, c+dc

                    if (
                        0 <= nr < n and
                        0 <= nc < n and
                        not visited[nr][nc] and
                        dist[nr][nc] >= limit
                    ):
                        visited[nr][nc] = True
                        q.append((nr,nc))

            return False

        # --------------------------
        # Step 3: Binary Search
        # --------------------------
        low = 0
        high = max(max(row) for row in dist)

        ans = 0

        while low <= high:

            mid = (low + high)//2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans