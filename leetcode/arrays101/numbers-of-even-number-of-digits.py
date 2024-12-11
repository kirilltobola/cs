from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            n = num
            cnt_digits = 0
            while n > 0:
                n //= 10
                cnt_digits += 1
            
            if not cnt_digits % 2:
                result += 1
        return result
