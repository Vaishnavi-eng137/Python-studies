class Employee:

    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self,name,salary):
    #instance variables or instance attributes
       self.emp_name = name           #self (means current object) pointing to each object
       self.emp_salary = salary

    #method of a class
    def displayEmployeeInfo(self):
        print("Employee name: ",self.emp_name,",Employee Salary: ",self.emp_salary)

#How we create a object
emp1 = Employee("Shalu",1000)
emp2 = Employee("Neha",3000)

emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()

print(emp1.emp_name)
print(emp2.emp_name)

#Difference between class variable and instance variable

