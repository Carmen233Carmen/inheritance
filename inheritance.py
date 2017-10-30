# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:30:31 2017

@author: Gu
"""

class Employee:
    
    __num_of_emps = 0
    _raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.__pay = pay
        Employee.__num_of_emps += 1
        
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.__pay = int(self.__pay * self._raise_amt)
    
    @classmethod
    def totalEmp(cls):
        return cls.__num_of_emps
     
    def info(self):
        print(self.fullname)
        print(self.__pay)    
        
#    @property
#    def get_pay(self):
#        return self._pay

class Developer(Employee):
    
    _raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #alternatively: Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
    
#    def get_pay(self):
#        return self._pay    

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("No such an employee.")
            
#    @property
    def print_emps(self):
        for employee in self.employees:
            print('--> {}, {}, salary:{}'.format(employee.fullname, employee.prog_lang, employee.get_pay()))
        
        
            

emp_1 = Developer("Johnny", "English", 1000, 'Python')
emp_2 = Developer("James", "Bond", 1000, "Java") 
emp_3 = Manager("Donald", "Trump", 2000)

emp_3.add_employee(emp_1)
emp_3.add_employee(emp_2)