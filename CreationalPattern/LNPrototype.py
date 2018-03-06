# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# python设计模式之原型模式
# Pototype模式
# 假如你爱玩游戏，你能想到游戏里面有很多的角色，但是其实你有没有注意:脸型，身材，眼睛..这些其实都是略有不同的搭配， 这也就是原型的作用：不需要你每次都制造一个复杂的人物，只是根据一个原型的人物做些简单的修改即可

# 这里肯定要做深拷贝，要不然python的就是对象的引用
from copy import deepcopy

class Prototype:
    def __init__(self):
        self._objs = {}

    def registerObject(self, name, obj):
        """注册对象"""
        self._objs[name] = obj

    def unregisterObject(self, name):
        """取消注册"""
        del self._objs[name]

    def clone(self, name, **attr):
        """克隆对象"""
        obj = deepcopy(self._objs[name])
        # 但是会根据attr增加或覆盖原对象的属性
        obj.__dict__.update(attr)
        return obj

if __name__ == '__main__':
    class A:
        pass

    a=A()
    prototype=Prototype()
    prototype.registerObject("a",a)
    b=prototype.clone("a",a=1,b=2,c=3)

    # 这里会返回对象a
    print(a)
    # 这里的对象其实已经被修改成(1, 2, 3)
    print(b.a, b.b, b.c)