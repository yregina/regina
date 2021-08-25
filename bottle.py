class  Bottle:
    __height = ""
    __volume = ""
    __color = ""
    __material = ""

    def setheight(self,height):
        if height < 0:
            print("高度非法，别瞎弄！")
        else:
            self.__height = height
    def getheight(self):
        return self.__height
    def setvolume(self,volume):
        if volume < 0:
            print("容积非法，别瞎弄！")
        else:
            self.__volume = volume
    def getvolume(self):
        return self.__volume
    def setcolor(self,color):
        self.__color = color
    def getcolor(self):
        return self.__color
    def setmaterial(self,material):
        self.__material = material
    def getmaterial(self):
        return self.__material

    def store(self,liquids):
        print(self.__material,"的水杯能存放",liquids)

b = Bottle()
b.setheight(15)
b.setvolume(600)
b.setcolor("蓝色")
b.setmaterial("塑料")
b.store("肥宅快乐水")