from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        _max = -1
        for i in range(len(arr) - 1, -1, -1):
            next_max = max(_max, arr[i])
            arr[i] = _max
            _max = next_max
        return arr
