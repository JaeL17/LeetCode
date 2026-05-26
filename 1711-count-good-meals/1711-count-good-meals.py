from collections import defaultdict
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        answer:int = 0
        mod:int = 10**9 + 7
        powers:List[int] = [2**i for i in range(22)]
        count = defaultdict(int)

        for food in deliciousness:
            for power in powers:
                target = power - food
                answer += count[target]
            count[food] +=1

        return answer % mod

        