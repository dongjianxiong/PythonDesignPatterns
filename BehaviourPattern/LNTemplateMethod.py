# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'


# 在模板模式（Template Pattern）中，一个抽象类公开定义了执行它的方法的方式/模板。它的子类可以按需要重写方法实现，但调用将以抽象类中定义的方式进行。这种类型的设计模式属于行为型模式。
#
# 意图：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
#
# 主要解决：一些方法通用，却在每一个子类都重新写了这一方法。
#
# 何时使用：有一些通用的方法。
#
# 如何解决：将这些通用算法抽象出来。
#
# 关键代码：在抽象类实现，其他步骤在子类实现。
#
# 应用实例： 1、在造房子的时候，地基、走线、水管都一样，只有在建筑的后期才有加壁橱加栅栏等差异。 2、西游记里面菩萨定好的 81 难，这就是一个顶层的逻辑骨架。 3、Spirng 中对 Hibernate 的支持，将一些已经定好的方法封装起来，比如开启事务、获取 Session、关闭 Session 等，程序员不重复写那些已经规范好的代码，直接丢一个实体就可以保存。
#
# 优点： 1、封装不变部分，扩展可变部分。 2、提取公共代码，便于维护。 3、行为由父类控制，子类实现。
#
# 缺点：每一个不同的实现都需要一个子类来实现，导致类的个数增加，使得系统更加庞大。
#
# 使用场景： 1、有多个子类共有的方法，且逻辑相同。 2、重要的、复杂的方法，可以考虑作为模板方法。

# 模板方法模式概述
#        在现实生活中，很多事情都包含几个实现步骤，例如请客吃饭，无论吃什么，一般都包含点单、吃东西、买单等几个步骤，通常情况下这几个步骤的次序是：点单 --> 吃东西 --> 买单。在这三个步骤中，点单和买单大同小异，最大的区别在于第二步——吃什么？吃面条和吃满汉全席可大不相同，如图1所示：
#
# 图1 请客吃饭示意图
#         在软件开发中，有时也会遇到类似的情况，某个方法的实现需要多个步骤（类似“请客”），其中有些步骤是固定的（类似“点单”和“买单”），而有些步骤并不固定，存在可变性（类似“吃东西”）。为了提高代码的复用性和系统的灵活性，可以使用一种称之为模板方法模式的设计模式来对这类情况进行设计，在模板方法模式中，将实现功能的每一个步骤所对应的方法称为基本方法（例如“点单”、“吃东西”和“买单”），而调用这些基本方法同时定义基本方法的执行次序的方法称为模板方法（例如“请客”）。在模板方法模式中，可以将相同的代码放在父类中，例如将模板方法“请客”以及基本方法“点单”和“买单”的实现放在父类中，而对于基本方法“吃东西”，在父类中只做一个声明，将其具体实现放在不同的子类中，在一个子类中提供“吃面条”的实现，而另一个子类提供“吃满汉全席”的实现。通过使用模板方法模式，一方面提高了代码的复用性，另一方面还可以利用面向对象的多态性，在运行时选择一种具体子类，实现完整的“请客”方法，提高系统的灵活性和可扩展性。
#        模板方法模式定义如下：
# 模板方法模式：定义一个操作中算法的框架，而将一些步骤延迟到子类中。模板方法模式使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
#
# Template Method Pattern:  Define the skeleton of an algorithm in an  operation, deferring some steps to subclasses. Template Method lets  subclasses redefine certain steps of an algorithm without changing the  algorithm's structure.
#        模板方法模式是一种基于继承的代码复用技术，它是一种类行为型模式。
#        模板方法模式是结构最简单的行为型设计模式，在其结构中只存在父类与子类之间的继承关系。通过使用模板方法模式，可以将一些复杂流程的实现步骤封装在一系列基本方法中，在抽象父类中提供一个称之为模板方法的方法来定义这些基本方法的执行次序，而通过其子类来覆盖某些步骤，从而使得相同的算法框架可以有不同的执行结果。模板方法模式提供了一个模板方法来定义算法框架，而某些具体步骤的实现可以在其子类中完成。
#

class Register(object):
    '''用户注册接口'''

    def register(self):
        pass

    def login(self):
        pass

    def auth(self):
        self.register()
        self.login()


class RegisterByQQ(Register):
    '''qq注册'''

    def register(self):
        print("---用qq注册-----")

    def login(self):
        print('----用qq登录-----')


class RegisterByWeiChat(Register):
    '''微信注册'''

    def register(self):
        print("---用微信注册-----")

    def login(self):
        print('----用微信登录-----')


if __name__ == "__main__":
    register1 = RegisterByQQ()
    register1.login()

    register2 = RegisterByWeiChat()
    register2.login()