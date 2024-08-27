from typing import List


def sort_merge(array: List[int]):
    """归并排序.

    Args:
        array (List[int]): _description_

    Returns:
        _type_: _description_
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = sort_merge(array[:mid])
    right = sort_merge(array[mid:])
    return merge_list(left, right)


def merge_list(left: List[int], right: List[int]):
    answer = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            answer.append(left[i])
            i += 1
        else:
            answer.append(right[j])
            j += 1
    if i < len(left):
        answer.extend(left[i:])
    if j < len(right):
        answer.extend(right[j:])
    return answer


def quick_sort(array: List[int]):
    """快速排序.

    Args:
        array (List[int]): _description_

    Returns:
        _type_: _description_
    """
    import random

    def quick_sort_inplace(arr, left, right):
        flag = arr[random.randint(left, right)]
        i, j = left, right
        while i <= j:
            while arr[i] < flag:
                i += 1
            while arr[j] > flag:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if i < right:
            quick_sort_inplace(arr, i, right)
        if j > left:
            quick_sort_inplace(arr, left, j)

    return quick_sort_inplace(array, 0, len(array) - 1)


def heapify(array: List[int], n: int, i: int):
    """调整堆.

    Args:
        array (List[int]): _description_
        n (int): 列表中元素的个数.
        i (int): 对索引为i的节点进行调整.
    """
    parent = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and array[left] > array[parent]:
        parent, left = left, parent
    if right < n and array[right] > array[parent]:
        parent, right = right, parent
    if i != parent:
        array[i], array[parent] = array[parent], array[i]
        heapify(array, n, parent)


def build_heap(array: List[int], n: int):
    """构建堆.

    Args:
        array (List[int]): _description_
        n (int): _description_
    """
    last = n - 1
    parent = (last - 1) // 2
    for i in range(parent, -1, -1):
        heapify(array=array, n=n, i=i)


def heap_sort(array: List[int]):
    """堆排序

    Args:
        array (List[int]): 要排序的数组.
    """
    n = len(array)
    build_heap(array, n)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(arr, i, 0)


if __name__ == "__main__":
    # a = [1, 3, 5, 2, 1, 1, 6, 2, 4]
    # b = sort_merge(a)
    # print(b)
    # a = [1, 3, 5, 2, 1, 1, 6, 2, 4]
    # quick_sort(a)
    # print(a)
    # 示例
    arr = [4, 10, 3, 5, 1, 2]
    print("原始数组:", arr)
    heap_sort(arr)
    print(arr)
    # print("堆排序后:", arr)
