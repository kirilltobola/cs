from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        cur_cnt = 0
        
        for i in nums:
            if i == 1:
                cur_cnt += 1
            else:
                max_cnt = max(max_cnt, cur_cnt)
                cur_cnt = 0
        return max(max_cnt, cur_cnt)
