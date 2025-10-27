class mymaths:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        sum=self.a+self.b
        print(sum)

    def subtract(self):
        subtract=self.a-self.b
        print(subtract)

    def multiply(self):
        multiply=self.a*self.b
        print(multiply)

    def divide(self):
        divide=self.a//self.b
        print(divide)

result=mymaths(10,5)
result.add()    
result.subtract()
result.multiply()
result.divide()