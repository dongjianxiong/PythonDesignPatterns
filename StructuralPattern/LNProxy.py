# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

#
# 代理模式
# 应用特性：需要在通信双方中间需要一些特殊的中间操作时引用，多加一个中间控制层。
# 结构特性：建立一个中间类，创建一个对象，接收一个对象，然后把两者联通起来

class sender_base(object):
    def __init__(self):
        pass

    def send_something(self):
        pass


class send_class(sender_base):

    def __init__(self, receiver):
        self.receiver = receiver

    def send_something(self, something):
        print("Send " + something + " to " + self.receiver.name)


class receive_class:
    name = ""
    def __init__(self, name):
        self.name = name


class agent_calss(sender_base):

    def __init__(self, receiver):
        self.send_obj = send_class(receiver)

    def send_something(self, something):
        self.send_obj.send_something(something)


if '__main__' == __name__:
    receiver = receive_class('Lenny')
    agent = agent_calss(receiver)
    agent.send_something('agentinfo')

    print(receiver.__class__)
    print(agent.__class__)


