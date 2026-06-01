from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        min_cost = 0

        for i in range(len(cost)):
            if i % 3 != 2:
                min_cost += cost[i]

        return min_cost