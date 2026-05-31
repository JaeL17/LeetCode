class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer: List[List[int]] = []
        intervals.sort()
        if len(intervals) == 1:
            return [[intervals[0][0], intervals[0][1]]]

        idx = 1
        start_prev = intervals[0][0]
        end_prev = intervals[0][1]
        while idx <= len(intervals)-1:

            # check whether there is an overlap between current and previous intervals
            start_current = intervals[idx][0]
            end_current = intervals[idx][1]

            if idx == len(intervals)-1:
                if end_prev >= start_current: # we can merge
                    answer.append([start_prev, max(end_current, end_prev)])

                else: # we cant merge, no overlap
                    answer.append([start_current, end_current])

            if end_prev >= start_current: # we can merge
                end_prev = max(end_prev, end_current) # update the max range

            else: # we cant merge, no overlap
                answer.append([start_prev, end_prev])
                start_prev = start_current
                end_prev = end_current
            idx +=1

        return answer
