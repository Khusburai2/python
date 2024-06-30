# # class Calculation:
# #     def add(self,a,b):
# #         return a+b
# #     def sub(self,a,b):
# #         return a-b
# #     def multi(self,a,b):
# #         return a*b
    
# # calculator = Calculation()
# # mero_calculator = Calculation()
# # result2 = calculator.add(1,2)
# # result3 = calculator.sub(1,2)
# # result4 = calculator.multi(1,2)
# # print(result2)
# # print(result3)
# # print(result4)


# # class Looping:
# #     def __init__(self, sumlist):
# #         self.sumlist = sumlist

# #     def list(self):
# #         for i in self.sumlist:
# #             print(i)

# #     def cub(self):
# #         for i in self.sumlist:
# #             print(i**3)

# # look = Looping([2, 3])
# # look.list()
# # look.cub()
# # look.sumlist = [4, 5, 6, 78]


 






# class Animal():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


#     def Sound(self):
#         print(self.name)
#         print(self.age)

# anime = Animal('dog',14)
# anime.Sound()



# class Monkey(Animal):
#     def __init__(self,name,age,live):
#         self.eat



# poly










class Shape():
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius **2 

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width


    def area(self):
            return self.length * self.width

def print_area(Shape):
     print("area:",Shape.area())

rectangle = Rectangle(5,2)
circle = Circle(4)


print_area(rectangle)
print_area(circle)
            
class Animal:
     def speak(self):
          pass
class Dog(Animal):
     def speak(self):
          return "woof"
     
class Cat(Animal):
     def speak(self):
          return"meow"


def make_sound(animal):
     print(animal.speak())

animals = [Dog(),Cat()]
for animal in animals:
     make_sound(animal)              


class Employee:
     def __init__(self,name):
          self.name = name

     def cal_salary(self):
          pass

class FullEmployee(Employee):
     def cal_salary(self):
          return 50000


class PartEmployee(Employee):
     def cal_salary(self):
          return 25000

employees = [FullEmployee('Bob'),PartEmployee('pranjal')]
for employee in employees:
     print(f"{employee.name} salary",employee.cal_salary())                    
