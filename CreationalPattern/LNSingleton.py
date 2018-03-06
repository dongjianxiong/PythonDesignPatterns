# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# 意图：
#
# 保证一个类仅有一个实例，并提供一个访问它的全局访问点。
#
# 适用性：
#
# 当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时。
#
# 当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时。

#实现__new__方法
#并在将一个类的实例绑定到类变量_instance上,
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
#如果cls._instance不为None,直接返回cls._instance

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


instance_1 = MyClass("Alun")
instance_2 = MyClass("Lenny")

print (instance_1.name)
print (instance_2.name)

