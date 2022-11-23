class Employee:

    #Class attribute
    empCount = 0

    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self,name,salary):
    #instance variables or instance attributes
       self.emp_name = name           #self (means current object) pointing to each object
       self.emp_salary = salary
       Employee.empCount += 1

    #method of a class
    def displayEmployeeInfo(self):
        print("Employee name: ",self.emp_name,",Employee Salary: ",self.emp_salary)

    
    #method of a class
    def displayEmployeeCount(self):
        print("Employee count: ", Employee.empCount)

#How we create a object
emp1 = Employee("Shalu",1000)
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

emp2 = Employee("Neha",3000)
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()

emp1.displayEmployeeCount()
emp2.displayEmployeeCount()

#print instance variables of a object
print(emp1.emp_name)
print(emp1.emp_salary)
print(emp2.emp_name)
print(emp2.emp_salary) 

#Lets access Class variable from instance itself
print(emp1.empCount)
print(emp2.empCount)

emp1.empCount = 10
emp2.empCount = 20

print(emp1.empCount)
print(emp2.empCount)

# what is static method in python?
class Car:
    def __init__(self,name,color):
        self.car_name = name
        self.car_color = color
    
    def displayCarDetails(self):
        print("Car name is",self.car_name,"and car color is",self.car_color)
    
    @staticmethod
    def initialMessage():
        print("Nice car !!!")

Car.initialMessage()
car1 = Car('XUV 700','WHITE')
car1.displayCarDetails()

#THIS WILL NOT WORK
#Car.displayCarDetails()

#ineuron company
class Employee:

    @staticmethod
    def isEmployeeOf():
        print("Employee class for ineuron !!")

Employee.isEmployeeOf()

class Calcultion:
    @staticmethod
    def addTwoNums(num1,num2):
        print("Sum of two numbers =",num1 +num2)

Calcultion.addTwoNums(22,2)
