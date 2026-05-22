import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binary search between min and max hours possible 
        left = 1
        right = max(piles)

        def can_finish(k: int) -> bool:
            hours = 0
            for pile in piles:
                # ceil division: how many hours needed for this pile
                hours += math.ceil(pile/k)
            return hours <= h

        answer = right
        # Time complexity: O(n log m)
        # n = number of piles
        # m = max(piles)
        while left <= right:
            mid = (left + right) // 2

            if can_finish(mid):
                answer = mid
                right = mid -1
            else:
                left = mid + 1


        return answer