from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        left = 0
        right = len(arr) - 1
        
        for i in range(len(arr)):
            if left == right:
                break
            if arr[left + 1] > arr[left]:
                left += 1
    
            if arr[right - 1] > arr[right]:
                right -= 1
        if left == 0 or right == len(arr) - 1:
            return False
        return left == right
