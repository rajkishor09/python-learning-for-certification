class Classy:
    def visible(self):
        print("visible")

    def __hidden(self): # private method
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed to call __hidden")

obj._Classy__hidden()