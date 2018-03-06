# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# 每一个模式都是针对一定问题的解决方案。抽象工厂模式与工厂方法模式的最大区别就在于，工厂方法模式针对的是一个产品等级结构；而抽象工厂模式则需要面对多个产品等级结构。
#
# 　　在学习抽象工厂具体实例之前，应该明白两个重要的概念：产品族和产品等级。
# 在什么情况下应当使用抽象工厂模式
# 　　1.
# 一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节，这对于所有形态的工厂模式都是重要的。
#
# 　　2.
# 这个系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。
#
# 　　3.
# 同属于同一个产品族的产品是在一起使用的，这一约束必须在系统的设计中体现出来。（比如：Intel主板必须使用Intel
# CPU、Intel芯片组）
#
# 　　4.
# 系统提供一个产品类的库，所有的产品以同样的接口出现，从而使客户端不依赖于实现。
#
# 抽象工厂模式的起源
# 　　抽象工厂模式的起源或者最早的应用，是用于创建分属于不同操作系统的视窗构建。比如：命令按键（Button）与文字框（Text)都是视窗构建，在UNIX操作系统的视窗环境和Windows操作系统的视窗环境中，这两个构建有不同的本地实现，它们的细节有所不同。
#
# 　　在每一个操作系统中，都有一个视窗构建组成的构建家族。在这里就是Button和Text组成的产品族。而每一个视窗构件都构成自己的等级结构，由一个抽象角色给出抽象的功能描述，而由具体子类给出不同操作系统下的具体实现。
#
#
#
# 抽象工厂模式的优点
# 分离接口和实现
# 　　客户端使用抽象工厂来创建需要的对象，而客户端根本就不知道具体的实现是谁，客户端只是面向产品的接口编程而已。也就是说，客户端从具体的产品实现中解耦。
#
# 使切换产品族变得容易
# 　　因为一个具体的工厂实现代表的是一个产品族，比如上面例子的从Intel系列到AMD系列只需要切换一下具体工厂。
#
# 抽象工厂模式的缺点
# 不太容易扩展新的产品
# 　　如果需要给整个产品族添加一个新的产品，那么就需要修改抽象工厂，这样就会导致修改所有的工厂实现类。

class AbstractFactory(object):
    computer_name = ''

    def createCpu(self):
        pass

    def createMainboard(self):
        pass


class IntelFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer '

    def createCpu(self):
        return IntelCpu('I7-6500')

    def createMainboard(self):
        return IntelMainBoard('Intel-6000')


class AmdFactory(AbstractFactory):
    computer_name = 'Amd 4 computer '

    def createCpu(self):
        return AmdCpu('amd444')

    def createMainboard(self):
        return AmdMainBoard('AMD-4000')


class AbstractCpu(object):
    series_name = ''
    instructions = ''
    arch = ''


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AmdCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AbstractMainboard(object):
    series_name = ''


class IntelMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class AmdMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class ComputerEngineer(object):

    def makeComputer(self, computer_obj):
        self.prepareHardwares(computer_obj)

    def prepareHardwares(self, computer_obj):
        self.cpu = computer_obj.createCpu()
        self.mainboard = computer_obj.createMainboard()

        info = '''------- computer [%s] info:
    cpu: %s
    mainboard: %s

 -------- End --------
        ''' % (computer_obj.computer_name, self.cpu.series_name, self.mainboard.series_name)
        print(info)


if __name__ == "__main__":
    engineer = ComputerEngineer()

    computer_factory = IntelFactory()
    engineer.makeComputer(computer_factory)

    computer_factory2 = AmdFactory()
    engineer.makeComputer(computer_factory2)