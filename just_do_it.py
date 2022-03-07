

# 快速排序
def q_sort():
    def quick_sort(array, left, right):

        if left >= right:
            return

        base = array[left]
        low = left
        high = right

        while low < high:
            while low < high and array[high] > base:
                high -= 1
            array[low] = array[high]

            while low < high and array[low] < base:
                low += 1
            array[high] = array[low]

        array[low] = base

        quick_sort(array, left, low-1)
        quick_sort(array, low+1, right)

    array = [3, 1, 2, 6, 7, 9, 8, 5, 4, 0]

    quick_sort(array, 0, len(array)-1)
    print(array)


# 冒泡排序

def b_sort():
    def bubble_sort(array):
        for i in range(len(array)):
            for j in range(len(array) -i -1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

    array = [3, 1, 2, 6, 7, 9, 8, 5, 4, 0]
    bubble_sort(array)
    print(array)


# q_sort()
# b_sort()

# 写个带参数的装饰器
from functools import wraps
def outer(text):
    def dec(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print("fun name: {}, args: {}, kwargs: {}".format(func.__name__, args, kwargs))
            print("with args decorator, args: {}".format(text))
            return func(*args, **kwargs)
        return inner
    return dec


@outer("outer")
# @dec
def use_decorator(flag="input word"):
    print("this is decorated !!!", flag)


use_decorator("input")


# 写个单例模式
class Singleton(object):
    _isinstance = None

    def __new__(cls, *args, **kwargs):
        if not cls._isinstance:
            cls._isinstance = super().__new__(cls, *args, **kwargs)
        return cls._isinstance


s1 = Singleton()
s2 = Singleton()
print()


def singleton(cls):
    _isinstance = {}

    def _singleton(*args, **kwargs):
        if cls not in _isinstance:
            _isinstance[cls] = cls(*args, **kwargs)
        return _isinstance[cls]
    return _singleton

@singleton
class A(object):
    pass


s1 = A()
s2 = A()
print(id(s1), id(s2))


# 生成器实现斐波那契数列
def fib_():
    def yield_fib(max):
        before, after = 0, 1
        while after < max:
            yield after
            before, after = after, before + after

    def create_fib(max):
        y_f = yield_fib(max)
        for fib in y_f:
            print(fib)

    create_fib(20)


fib_()












