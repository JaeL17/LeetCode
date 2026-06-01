class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        min_cost: int = 0
        cost.sort(reverse= True)
        i = 0
        while True:
            # check the number of candies left
            if i + 2 <= len(cost) - 1: # next 3 candies available
                cost_two_candies = cost[i] + cost[i + 1]
                min_cost += cost_two_candies
            elif i + 1 <= len(cost) - 1: # next 2 candies available
                cost_two_candies = cost[i] + cost[i + 1]
                min_cost += cost_two_candies
            elif i == len(cost) - 1:
                min_cost += cost[i]
            else:
                break
            i += 3

        return min_cost