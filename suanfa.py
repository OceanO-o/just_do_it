# 给定一个包含n个数的排序数组，找出给定目标值target的其实和结束位。
# 如果目标值不在数组中，返回[-1, -1]
ll = [5, 7, 7, 8, 8, 10]  # target=8   返回[3, 4]


def find_target(array, key):
    if key not in array:
        return [-1, 1]
    start = 0
    end = 0
    for index, one in enumerate(array):
        if one == key:
            if start:
                end = index
            else:
                start = index
    if end < start:
        end = start
    return [start, end]


print(find_target(ll, 10))

# 滑动窗口最大值
# [1, 2, 7, 7, 8] 滑动窗口k=3 返回 [7,7,8]

from functools import reduce


def get_max(array, k):
    if len(array) <= k:
        return array

    max_v = reduce(lambda x, y: x + y, array[:k])
    res = array[:k]
    for one in range(1, len(array) - k):
        current = reduce(lambda x, y: x + y, array[one:one + k])
        if current > max_v:
            max_v = current
            res = array[one:one + k]
    return res


lll = [1, 9, 7, 7, 8]
print(get_max(lll, 2))
