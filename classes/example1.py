# Python OOP
import datetime
class Employee:
    raiseamount = 1.04
    def __init__(self,firstname: str,lastname: str,pay: float)-> None:
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.pay = pay
        self.email = str.lower(firstname + "." + lastname+"@company.com")

    def employeedetails(self):
        print(self.fullname)
        print(self.email)
        print(self.pay)

    def applyraise(self)-> None:
        self.pay = self.pay*Employee.raiseamount

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raiseamount = amount
    
    @staticmethod
    def is_workday(day):
        if(day.weekday() == 5 or day.weekday() == 6):
            return False
        return True

class Developer(Employee):
    def __init__(self, firstname: str, lastname: str, pay: float, prog_lang: str) -> None:
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang
    
    def get_prog_lang(self):
        return self.prog_lang

class Manager(Employee):

    def __init__(self, firstname: str, lastname: str, pay: float, employees= None) -> None:
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            return None
        else:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())







emp1 = Developer("Jitendar","Singh",2045000,"Python")
emp1.employeedetails()

mgr_1 = Manager('sue','smith',90000,[emp1])
mgr_1.print_emps()



# print(emp1.get_prog_lang())
# my_date = datetime.date(2021,6,19)
# print(Employee.is_workday(my_date))
# print(help(Developer))

# Employee.set_raise_amount(1.05)
# emp1.employeedetails()
# emp1.applyraise()
# print("Raise Applied")
# emp1.employeedetails()
# print(emp1.__dict__)
# emp1.raiseamount = 1.05
# print(emp1.__dict__)
