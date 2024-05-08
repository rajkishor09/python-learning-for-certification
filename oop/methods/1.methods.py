class Classy:
    def other(self):
        print("other")
    
    def method(self, par): # first param have to be self then other params  
        print("method:", par)
        self.other() # invoke other class method


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

