## 在什么时候需要使用 OOP？
    oop:对象是对一类事物的抽象，通过抽象将事物的属性和方法封装起来，当需要实现一个目的时，
    只需要通过对象，使用对象包含解决问题的方法即可,不需要一步一步去实现。
    1）当需要将某些数据和操作包装起来的时候  2）为了代码重用，避免冗余，易于维护，可扩展
## python 多态 
    https://wiki.jikexueyuan.com/project/explore-python/Class/inheritance_and_polymorphism.html
    继承可以拿到父类的所有数据和方法，子类可以重写父类的方法，也可以新增自己特有的方法。
    有了继承，才有了多态，不同类的对象对同一消息会作出不同的响应
    不同对象调用相同方法时会做出不同的响应，这就是多态的魅力
    是指调用某个方法时会根据实际对象的类型决定调用哪个版本的方法。
    class Animal(object):
        def run(self):
            print('Animal is running...')
    dog = Dog()  
    dog.run()
    cat = Cat()
    cat.run()
    def run_twice(animal):
        animal.run()
    python的多态与c++等强类型语言的多态很不一样，在静态类型语言里，我们可以编写一个函数，
    接受一个鸭子类型的对象，调用它的quack方法，而在Python这种使用鸭子类型的语言里，这样的
    函数可以接收任意类型的对象，只要这个对象具有quack方法就可以正常运行。 这么做的好处就
    是这个函数不依赖于某种类型，也不需要在函数中检查参数的具体类型。 这也是多态的一种形式，
    但这种多态的实现完全由程序员自己来约束，并没有语言上的约束。
    鸭子类型：不去关心这个对象是什么，而是关心这个对象能够做什么
## isinstance 和 type
    isinstance(object,type-or-tuple-or-class) -> bool 判断一个对象是某个类或子类的实例。
    isinstance (a,int)
    isinstance (a,(str,int,list)) 第二个参数为一个元组类型，若对象类型与元组中类型名之一相同即返回True
    isinstance (a,class) 
    type(object) -> 类型 得到传入的object的类型
    共同点
    type和isinstance都可以判断变量是否属于某个内建类型
    不同点
    (1)type只接收一个参数,可以得到参数变量未知的所属的类型；
    而isinstance只能判断是否属于某个已知类型，不能直接得到变量未知的所属的类型
    (2)isinstance可以判断子类实例对象是属于父类的；而type会判断子类实例对象和父类类型不一样
    综上所述，isinstance和type的应用场景是不同的：
    type主要用于获取未知变量的类型
    isinstance主要用于判断A类是否继承于B类
    
##在什么时候使用类装饰器？
##你用过元类嘛？
##在什么时候用静态方法什么时候使用类方法？
##你了解那些管理属性？__call__ , __init__ , __new__ 都是在什么时候被触发？__getattr__ 和 __getattribute__ 应用有什么不同？
##你知道标准库里面的多少个模块？你能在需要的时候知道这个功能其实标准库里面已经实现了？
##什么时候用回调？
什么时候用 signal？假如你会 django 你知道 django 的 signal 是什么？你了解 orm 嘛？
asyncore，contextlib， functools， collections， heapq，itertools， SocketServer， weakref，operator (知道 3 个就算) 这些你会几个？
python 的多态是什么？
在什么场景可以尝试 python 的设计模式中的 XX (能想到 2 个场景就算)?
在什么时候可以使用 Mixin？
## 在什么时候可以使用 python 的闭包？
    闭包描述的是：脱离了函数本身的作用范围，局部变量还可以被访问得到
    def print_msg():
        # print_msg 是外围函数
        msg = "zen of python"        msg相对于printer()函数来说，是函数外的全局变量
        def printer():
            # printer 是嵌套函数
            print(msg)
        return printer

    another = print_msg()
    # 输出 zen of python
    another()
    一般情况下，函数中的局部变量仅在函数的执行期间可用，一旦 print_msg() 执行过后，
    我们会认为 msg变量将不再可用。然而，在这里我们发现 print_msg 执行完之后，在调
    用 another 的时候 msg 变量的值正常输出了，这就是闭包的作用，闭包使得局部变量
    在函数外被访问成为可能。
    
# 你曾经用过 yield 嘛？生成器和迭代器的区别和应用场景是什么？

    项目中如何使用yield，使用的思路就是，中断代码执行，在yield之前打开一个资源，
    然后在yield之后关闭这个资源， 这样可以很好地保证每次只有一个资源被打开，同
    时执行完成之后资源会被关闭. 第二个思路，就是节约内存，不要一下子加载所有的资源
    
    这是tornado的例子
    def get_all(self):
       """Returns an iterable of all (name, value) pairs.
    
        If a header has multiple values, multiple pairs will be
        returned with the same name.
        """
        for name, list in self.headers.iteritems():
            for value in list:
                之前我们可能自己定义一个list，然后把(name, value)extend到list中，
                现在只需要返回生成器，迭代get_all的返回值，就可以获取到一个list
                yield(name, value)
    
    在python的上下文管理中，经常会使用到yield
    @contextlib.contextmanager
    def session_stack():
        if not hasattr(db_ctx, 'session_stack'):
            db_ctx.session_stack = 0
    
        try:
            # yield之前，创建资源 + 1
            db_ctx.session_stack += 1
            yield
        finally:
            # yield之后，销毁资源 - 1
            db_ctx.session_stack -= 1

在什么可以使用 python 的函数式编程？
future 模块里面都有什么定义的用法？

py2和py3区别 
    统一了字符编码
    增加了新语法
    修改了一些语法
    去掉了一些语法  增加/去掉/修改了一些模块  模块改名 优化
    
进阶书籍
    https://www.dongwm.com/post/63/
