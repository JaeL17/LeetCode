from typing import List, Dict
import random

class RandomizedSet:

    def __init__(self):
        self.nums: List[int] = []
        self.index_map: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.index_map[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        remove_index = self.index_map[val]
        last_value = self.nums[-1]

        self.nums[remove_index] = last_value
        self.index_map[last_value] = remove_index

        self.nums.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)