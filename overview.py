# 线程池
from multiprocessing.pool import ThreadPool   # 相当于from multiprocessing.dummy import Process
pool = ThreadPool(5)
pool.apply_async(lambda x: x * x, ("args1", 'args2',))

# super函数  https://wiki.jikexueyuan.com/project/explore-python/Class/super.html
#      Base
#      /  \
#     /    \
#    A      B
#     \    /
#      \  /
#       C
"""
    子类调用super时，子类中会维护一个MRO列表，[C, A, B, Base],依次调用列表中的每一个
    而不是说super调用父类的方法，要是这样那么调用顺序为c,a,base,事实上是[C, A, B, Base]
    def super(cls, inst):
        mro = inst.__class__.mro()
        return mro[mro.index(cls) + 1]
        查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]
    事实上super里面实现的是：获取 inst 的 MRO 列表
    查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]
"""


#  __slots__
class Slots(object):
    __slots__ = "name", "age"

    def __init__(self, name, age):
        self.name = name
        self.age = age


"使用 __slots__ 来告诉 Python 只给一个固定集合的属性分配空间, 不能动态绑定的属性"
"__slots__ 设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了 slots，这样，"
"子类允许定义的属性就是自身的 slots 加上父类的 slots。"

slots = Slots("keke", 24)
slots.job = "computer"


# 元类 https://wiki.jikexueyuan.com/project/explore-python/Class/metaclass.html
# 类是实例对象的模板，元类是类的模板

# +----------+             +----------+             +----------+
# |          | instance of |          | instance of |          |
# | instance +------------>+  class   +------------>+ metaclass|
# |          |             |          |             |          |
# +----------+             +----------+             +----------+
class PrefixMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 给所有属性和方法前面加上前缀 my_
        _attrs = (('my_' + name, value) for name, value in attrs.items())

        _attrs = dict((name, value) for name, value in _attrs)  # 转化为字典
        _attrs['echo'] = lambda self, phrase: phrase  # 增加了一个 echo 方法
        # type 除了可以返回对象的类型，它还可以被用来动态地创建类（对象）
        return type.__new__(cls, name, bases, _attrs)  # 返回创建后的类
# py2
class Foo(object):
    __metaclass__ = PrefixMetaclass
    name = 'foo'
    def bar(self):
        # print 'bar'
        pass
# py3
# class Foo(metaclass=PrefixMetaclass):
#     name = 'foo'
#     def bar(self):
#         # print 'bar'
#         pass


"Python 会首先在当前类中寻找 __metaclass__，如果没有找到，就会在父类中寻找 __metaclass__"
"如果找不到，如此继续下去，如果在任何父类都找不到 __metaclass__，就会到模块层次中寻找，"
"如果还是找不到，就会用 type 来创建这个类。"
# 元类主要做了三件事：
# 拦截类的创建
# 修改类的定义
# 返回修改后的类
# 当你创建类时，解释器会调用元类来生成它，定义一个继承自 object 的普通类意味着调用 type 来创建它


# 字符编码 python2 和 python3
# https://wiki.jikexueyuan.com/project/explore-python/Basic/character_encoding.html
"""
    >>> import sys
    >>> sys.getdefaultencoding()
    py2 'ascii'  py3 'utf-8'
"""
# Python2 中有两种和字符串相关的类型：str 和 unicode
# +----------+             +----------+
# |     ascii|    decode   |          |
# | str gbk  +------------>+ unicode  +
# |     utf8 |<------------|          |
# |  字节码  |    encode   |          |
# +----------+             +----------+
# 在python2中，x = "hello",  chardet.detect(x), 'encoding': 'ascii'   默认使用ascii编码
#              x = b"hello"  chardet.detect(x), 'encoding': 'ascii'
#              x = "你好"， chardet.detect(x)   'encoding': 'utf-8'  中文则采用utf-8编码
#              x = u"你好"  type(x) = unicode
#  coding:utf-8,用来保证文件中可以使用中文，将中文进行转码成utf-8  sys.getdefaultencoding() 依然为ascii
#  sys.setdefaultencoding(utf-8) 直接更改了当前默认编码格式,   sys.getdefaultencoding() 则为utf-8
#  在进行同时包含 str 类型和 unicode 类型的字符串操作时，Python2 一律都把 str 解码（decode）
# 成 unicode 再运算，这时就很容易出现 UnicodeDecodeError。
# >>> s = '你好'    # str 类型, utf-8 编码
# >>> u = u'世界'   # unicode 类型
# >>> s + u        # 会进行隐式转换，即 s.decode('ascii') + u
# Traceback (most recent call last):
# 正确做法  s.decode('utf-8') + u

# 如果函数或类等对象接收的是 str 类型的字符串，但你传的是 unicode，Python2 会默认使用 ascii
# 将其编码成 str 类型再运算，这时就很容易出现 UnicodeEncodeError。
# >>> u_str = u'你好'
# >>> str(u_str)
# Traceback (most recent call last):
# 正确做法  str(u_str.encode('utf-8'))

# 参数魔法
# 它们在使用的时候是有顺序的，依次是必选参数、默认参数、可变参数和关键字参数。
# >>> def func(x, y, z=0, *args, **kwargs):  *() **{}, 打包，使用时解包
# func(1, 2, 3, 4, 5, 6) x=1, y=2, z=3, args=(4, 5, 6), kwargs={}


# 高阶函数
# 在函数式编程中，我们可以将函数当作变量一样自由使用。一个函数接收另一个函数作为参数，
# 这种函数称之为高阶函数
# map(function, sequence)
# 对 sequence 中的 item 依次执行 function(item)，并将结果组成一个 List 返回，也就是
map(lambda x: x * x, [1, 2, 3, 4])   # 使用 lambda     lamda args:

# reduce(function, sequence[, initial])
# 先将 sequence 的前两个 item 传给 function，即 function(item1, item2)，函数的返回值和
# sequence 的下一个 item 再传给 function， reduce(lambda x, y: x * y, [1, 2, 3, 4])
#                                          相当于 ((1 * 2) * 3) * 4
# filter 函数用于过滤元素，filter(function, sequnce)
even_num = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# 将 function 依次作用于 sequnce 的每个 item，即 function(item)，将返回值为 True 的
# item 组成一个 List/String/Tuple (取决于 sequnce 的类型，python3 统一返回迭代器) 返回。


# 深浅拷贝
#   赋值是引用，一个更改另一个也更改。
#   浅拷贝，重新开辟空间存储被拷贝的值，但列表中的列表会指向源列表中的列表，及引用
#   及，开辟新空间存储123456，456还是指向原来的456的地址，改变123各值，两个列表不会受到影响
#   改变456的值，两个列表都将改变
#   深拷贝，则会创建新的456存储空间，各个列表至此没有一点关系
import copy
shadow_copy = [1, 2, 3, [4, 5, 6]]
sha = shadow_copy.copy()
print(sha,   "    ", shadow_copy)

# sha[0] = 100
# print(sha,    "    ", shadow_copy)

# sha[3][0] = "shadow"
# print(sha, "   ", shadow_copy)

deep = copy.deepcopy(shadow_copy)
deep[3][0] = "shadow"
print(deep, "   ", shadow_copy)

# 偏函数
"""
from functools import partial

def subtraction(x, y):
    return x - y

f = partial(subtraction, 4)  # 4 赋给了 x
partial 的功能：固定函数参数，返回一个新的函数
"""

# 迭代器
# 迭代器是指遵循迭代器协议（iterator protocol）的对象 实现了__iter()__和 next()方法（在 Python3 中是 __next__() 方法）
# 迭代器不会把数据全部加载到内存，而是用到某一个才会取读取值
# 生成器
# 它有两种构造方式：生成器表达式，numbers = (x for x in range(5))  生成器函数 含有 yield 关键字的函数
# yield 把函数变成了一个生成器。
# 生成器函数的执行过程看起来就是不断地 执行->中断->执行->中断 的过程。
# 一开始，调用生成器函数的时候，函数不会立即执行，而是返回一个生成器对象；
# 然后，当我们使用 next() 作用于它的时候，它开始执行，遇到 yield 语句的时候，执行被中断，并返回当前的迭代值，
# 要注意的是，此刻会记住中断的位置和所有的数据，也就是执行时的上下文环境被保留起来；
# 当再次使用 next() 的时候，从原来中断的地方继续执行，直至遇到 yield，如果没有 yield，则抛出异常。


# 迭代器生成器实现斐波那契
def fib():
    x, y = 0, 1
    while True:
        x, y = y, x + y
        yield x

f = fib()
for key in f:
    if key < 10:
        print(key)


# 上下文管理器

"""
from math import sqrt, pow

class Point(object):
    def __init__(self, x, y):
        print 'initialize x and y'
        self.x, self.y = x, y

    def __enter__(self):
        print "Entering context"
        return self

    def __exit__(self, type, value, traceback):
        print "Exiting context"

    def get_distance(self):
        distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
        return distance
"""

# 通过yield实现
# from contextlib import contextmanager
#
# @contextmanager
# def point(x, y):
#     print 'before yield'
#     yield x * x + y * y
#     print 'after yield'
#
# with point(3, 4) as value:
#     print 'value is: %s' % value
#
# # output
# before yield
# value is: 25
# after yield

# 上下文管理器是支持上下文管理协议的对象，也就是实现了 __enter__ 和 __exit__ 方法。
# 通常，我们使用 with 语句调用上下文管理器。with 语句尤其适用于对资源进行访问的场景，
# 确保执行过程中出现异常情况时也可以对资源进行回收，比如自动关闭文件等。
# __enter__ 方法在 with 语句体执行前调用，with 语句将该方法的返回值赋给 as 字句中的变量，如果有 as 字句的话。
# __exit__ 方法在退出运行时上下文时被调用，它负责执行『清理』工作，比如关闭文件，释放资源等。
# 如果退出时没有发生异常，则 __exit__ 的三个参数，即 type, value 和 traceback 都为 None。如果发生异常，
# 返回 True 表示不处理异常，否则会在退出该方法后重新抛出异常以由 with 语句之外的代码逻辑进行处理。

#   __weakref__弱引用
# 首先先说下 weakref : 弱引用，与强引用相对，是指不能确保其引用的对象不会被垃圾回收器回收的引用。
# 一个对象若只被弱引用所引用，则被认为是不可访问（或弱可访问）的，并因此可能在任何时刻被回收.
# 在 Python 中，当一个对象的引用数目为 0 的时候，才会被从内存中回收。但是被循环引用呢？
