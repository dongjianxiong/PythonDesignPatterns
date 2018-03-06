# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# 意图
#
# 将一个类的接口转换成客户希望的另外一个接口。Adapter 模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
# 适用性：
#
# 你想使用一个已经存在的类，而它的接口不符合你的需求。
#
# 你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口可能不一定兼容的类）协同工作

class Animal(object):
    name = ""
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def eat(self):
        print("Eat something")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def eat(self):
        print("Eat meat")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    def eat(self):
        print("Eat fish")



#待适配类，getMyName(self) 和 eatFood(self)两个方法名称跟其他animal不一样，因此需要适配
class Pig(object):
    def __init__(self, name):
        self.name = name
    def getMyName(self):
        return self.name
    def eatFood(self):
        print("Eat every thing")


# 翻译（适配器），getMyName(self) 和 eatFood(self)两个方法名称替换成getName(self)和eat(self)，这样外部调用就可以保持统一
class Translator(Animal):
    pig = None
    def __init__(self, name):
        self.pig = Pig(name)
    def getName(self):
        return self.pig.getMyName()
    def eat(self):
        self.pig.eatFood()


dog = Dog("Dog")
cat = Cat("Kity")
pig = Translator("Nini")

print(dog.getName())
print(cat.getName())
print(pig.getName())
