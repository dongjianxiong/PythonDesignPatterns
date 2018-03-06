# coding:utf-8
#测试各个设计模式实现类

import  CreationalPattern.LNSimpleFactory
import  CreationalPattern.LNFactoryMethod

#简单工厂模式
# nameList = ["Dos", "Cat", "Chicken"]
# for name in nameList:
#
#     animal = CreationalPattern.LNSimpleFactory.OtherClass().creatAnimal(name)
#     if animal == None:
#         print "Not animal name %s", name
#     else:
#         animal.eat()

#工厂方法模式
doc = CreationalPattern.LNSimpleFactory.DogFactory().creatAnimal()
doc.eat()

cat = CreationalPattern.LNSimpleFactory.CatFactory().creatAnimal()
cat.eat()

chicken = CreationalPattern.LNSimpleFactory.ChickenFactory().creatAnimal()
chicken.eat()
