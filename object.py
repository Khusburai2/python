class Calculation:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multi(self,a,b):
        return a*b
    
calculator = Calculation()
mero_calculator = Calculation()
result2 = calculator.add(1,2)
result3 = calculator.sub(1,2)
result4 = calculator.multi(1,2)
print(result2)
print(result3)
print(result4)


class Looping:
    def __init__(self, sumlist):
        self.sumlist = sumlist

    def list(self):
        for i in self.sumlist:
            print(i)

    def cub(self):
        for i in self.sumlist:
            print(i**3)

look = Looping([2, 3])
look.list()
look.cub()
look.sumlist = [4, 5, 6, 78]


 

