class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter: dict[int, int] = dict()
        n = len(nums)
        
        # for loop: O(n) 
        for i in range(n):
            num = nums[i] # O(1)

            if num in counter:
                counter[num] +=1 # O(1)
            else:
                counter[num] = 1 # O(1)

        # for loop: O(k) 
        lst: List[Tuple[int, int]] = [(counter[key], key) for key in counter.keys()]
        
        # python sorting: O(k*log k) 
        lst.sort(reverse=True)
        lst = lst[:k]
        return [i[1] for i in lst]
        