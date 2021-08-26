'''
    生产消费者模型需求：造面包！
        厨师：3个厨师造面包，篮子容量500个，当篮子已满，等待2秒钟，然后继续判断是否已满若没有满，造一个加1
        用户：有6个用户，每个用户有3000元，每个面包2.5元，每个用户负责抢面包。当篮子面包不够，等待3秒继续抢，
             然后继续抢，一直到3000用完。
'''
from threading import Thread
import time

bread = 0


class Cook(Thread):
    __name = ""

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def run(self) -> None:
        global bread
        while True:
            if bread < 500:
                bread += 1
                print(self.__name + "做了一个面包，现在有" + str(bread) + "个面包\n", end='')
            else:
                time.sleep(2)


class Eat(Thread):
    __name = ""

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def run(self) -> None:
        global bread
        money = 3000
        eat = 0
        while True:
            if money >= 2.5 and bread > 0:
                money = money - 2.5
                bread = bread - 1
                eat = eat + 1
                print(self.__name + "抢了一个面包，现在有"+str(bread)+"个面包，他还有￥"+str(money)+"\n", end='')
            elif money < 2.5:
                print(self.__name + "抢了" + str(eat) + "个面包\n",end='')
                break
            else:
                time.sleep(3)



c1 = Cook()
c1.setName("小红")
c2 = Cook()
c2.setName("小明")
c3 = Cook()
c3.setName("小白")
e1 = Eat()
e1.setName("熊大")
e2 = Eat()
e2.setName("熊二")
e3 = Eat()
e3.setName("张三")
e4 = Eat()
e4.setName("李四")
e5 = Eat()
e5.setName("王五")
e6 = Eat()
e6.setName("赵六")
c1.start()
c2.start()
c3.start()
e1.start()
e2.start()
e3.start()
e4.start()
e5.start()
e6.start()
