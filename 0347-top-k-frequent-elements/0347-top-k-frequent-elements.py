from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count = Counter(nums)
        # count = count.most_common()
        # return [i[0] for i in count[:k]]

        counter: dict[int, int] = dict()
        n = len(nums)
        
        # for loop: O(n) 
        for i in range(n):
            num = nums[i] # O(1)

            if num in counter:
                counter[num] +=1 # O(1)
            else:
                counter[num] = 1 # O(1)

        # for loop: O(m) 
        lst: List[Tuple[int, int]] = [(counter[key], key) for key in counter.keys()]

        # python sorting: O(m*log m) 
        lst.sort(reverse=True)

        # list slicing: O(k) 
        lst = lst[:k]

        # total time complexity: O(n) + O(m) + O(m*log m) + O(k) =>  O(n + m log m), worst: O(n*log n)
        return [i[1] for i in lst]
        