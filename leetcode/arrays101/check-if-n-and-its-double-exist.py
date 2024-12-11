from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm = {}
        for i in arr:
            double_exist = hm.get(2 * i, False)
            double_exist |= hm.get(i / 2, False)
            if double_exist:
                return True
            hm[i] = True
        return False
