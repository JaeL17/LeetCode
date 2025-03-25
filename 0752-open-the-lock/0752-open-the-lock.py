from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        visited = set(["0000"])
        queue = deque([("0000", 0)])

        while queue:
            current, count = queue.popleft()

            for i in range(4):
                digit = int(current[i])
                for direction in [-1, 1]:
                    new_digit = (digit + direction) % 10
                    new_combo = current[:i] + str(new_digit) + current[i+1:]

                    if new_combo == target:
                        return count + 1
                    if new_combo not in visited and new_combo not in dead:
                        visited.add(new_combo)
                        queue.append((new_combo, count + 1))
        
        return -1
