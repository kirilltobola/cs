from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0
        right = len(arr) - 1
        
        for left in range(0, right - possible_dups):
            if arr[left] == 0:
                if left == right - possible_dups:
                    arr[right] = 0
                    right -= 1
                    break
                possible_dups += 1
        
        last = right - possible_dups
        for i in range(last, 0, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
