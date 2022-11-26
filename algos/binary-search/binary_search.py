
def binary_search(data: list, key: int) -> int:
    """
    left-hand binary search
    complexity O(logn)
    """
    left = -1
    right = len(data)
    while left < right - 1:
        mid = (left + right) // 2
        guess = data[mid]
        if guess < key:
            left = mid
        else:
            right = mid
    return right


if __name__ == '__main__':
    d = [1, 2, 3, 4, 5, 6]
    print(binary_search(d, 4))
