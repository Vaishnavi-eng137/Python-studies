class Employee:

    #Class attribute
    empCount = 0

    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self,name,salary):
    #instance variables or instance attributes
       self.emp_name = name           #self (means current object) pointing to each object
       self.emp_salary = salary
       Employee.empCount +=1

    #method of a class
    def displayEmployeeInfo(self):
        print("Employee name: ",self.emp_name,",Employee Salary: ",self.emp_salary)

    
    #method of a class
    def displayEmployeeCount(self):
        print("Employee count: ",Employee.empCount)

#How we create a object
emp1 = Employee("Shalu",1000)
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

emp2 = Employee("Neha",3000)
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()

emp1.displayEmployeeCount()
emp2.displayEmployeeCount()


