class  Computer:
    __brand = ""
    __size = ""
    __price = ""
    __cpu = ""
    __memory = ""
    __standbytime =""

    def setbrand(self, brand):
        self.__brand = brand
    def getbrand(self):
        return self.__brand
    def setsize(self,size):
        if size < 0:
            print("屏幕尺寸非法，别瞎弄！")
        else:
            self.__size = size
    def getsize(self):
        return self.__size
    def setprice(self, price):
        if price < 0:
            print("价格非法，别瞎弄！")
        else:
            self.__price = price
    def getprice(self):
        return self.__price
    def setcpu(self, cpu):
        self.__cpu = cpu
    def getcpu(self):
        return self.__cpu
    def setmemory(self,memory):
        if memory < 0:
            print("内存非法，别瞎弄！")
        else:
            self.__memory = memory
    def getmemory(self):
        return self.__memory
    def setstandbytime(self,standbytime):
        if standbytime < 0:
            print("内存非法，别瞎弄！")
        else:
            self.__standbytime = standbytime
    def getstandbytime(self):
        return self.__standbytime


    def typing(self,num):
        print(self.__brand,"正在打字，打了",num,"个字！")
    def playGame(self,game):
        print(self.__brand,"正在玩游戏，正在进行",game)
    def video(self,video):
        print(self.__brand,"正在看视频，正在观看",video)


c = Computer()

c.setsize(15)
c.setprice(6000)
c.setcpu("Intel酷睿i7")
c.setmemory(512)
c.setstandbytime(12)

c.typing(1000)
c.playGame("常回家看看")
c.video("陈情令")
