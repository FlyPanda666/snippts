from typing import List


def standard_binary_search(array: List[int], target: int):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


def lower_bound(array: List[int], target: int):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] == target:
            right = mid - 1
        else:
            right = mid - 1
    return left  # 也可以返回right + 1


if __name__ == "__main__":
    nums = [1, 2, 4, 6, 6, 9]
    answer = lower_bound(nums, 6)
    print(answer)
