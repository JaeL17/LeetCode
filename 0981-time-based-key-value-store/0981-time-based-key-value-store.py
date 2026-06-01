from typing import Dict, List, Tuple
import bisect

class TimeMap:

    def __init__(self):
        self.time_dict: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = []

        self.time_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""

        left = 0
        right = len(self.time_dict[key]) -1
        answer = ''
        while left <= right:
            mid = (right + left) // 2

            if self.time_dict[key][mid][0] <= timestamp:
                answer = self.time_dict[key][mid][1]

                left = mid +1
            else:
                right = mid -1


        return answer
        