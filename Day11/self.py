# Day11 of my 100DaysOfCode Challenge
# Program to use self parameter

class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 100K")

harry = Employee()
harry.getSalary()