#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:29:03 2017

@author: xg7
"""

#class Employee:
#    
#    def __init__(self, first, last):
#        self.first = first
#        self.last = last
#    
#    @staticmethod
#    def fullname(theFirstParameter):
#        return"{} {}".format(theFirstParameter.first,\
#               theFirstParameter.last)
#        
#emp_1 = Employee("Winnie", "The Pooh")

#print(emp_1.fullname())




#print("attributions of emp_1: {}".format(emp_1.__dict__))
#print("\nattributions of Employee: {}".format(Employee.__dict__))
#emp_1.raise_amd = 1.09
#print("\nif we set emp_1.raise_amt = 1.09\n")
#print("the attributions of emp_1: {}".format(emp_1.__dict__))

#class Employee:
#    
#    num_of_emps = 0
#    raise_amt = 1.04
#    
#    def __init__(self, first, last, pay):
#        self.first = first
#        self.last = last
#        self._pay = pay
#        Employee.num_of_emps += 1
# 
#    @property
#    def fullname(self):
#        return "{} {}".format(self.first, self.last)
#    
#    def apply_raise(self):
#        self._pay = int(self._pay * self.raise_amt)
#        
#    @classmethod
#    def from_string(cls, emp_str):
#        first, last, pay = emp_str.split('-')
#        return cls(first, last, int(pay))
#    
#    @staticmethod
#    def print_emp_info(emp):
#        print(emp.fullname)
#        print(emp._pay)    
#  
#
#emp_1 = Employee("Vladimir", "Putin", 1000)
#emp_2 = Employee.from_string("James-Comey-2000")
#
#
#Employee.print_emp_info(emp_1)
#Employee.print_emp_info(emp_2)



#    def apply_raise(self):
#        self.pay = int(self.pay * self.raise_amt)
      
#    @classmethod
#    def from_string(cls, emp_str):
#        first, last, pay = emp_str.split('-')
#        return cls(first, last, pay)
#        
#    
#    @property
#    def fullname(self):
#        return self.first + ' ' + self.last
#
#    @fullname.setter
#    def fullname(self, name):
#        first, last = name.split(" ")
#        self.first = first
#        self.last = last
#    

class Employee:
    
    num_of_emps = 0
    _raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self._pay = pay
        
    def apply_raise(self):
        self._pay = int(self._pay * self._raise_amt)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None
        

class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
    def change_prog_lang(self, new_prog_lang):
        self.prog_lang = new_prog_lang
        
        
emp_1 = Employee("Johnny", "English", 1000)
emp_2 = Developer("James", "Bond", 2000, "Python")   

emp_1.apply_raise()

isinstance(emp_1, Employee)
issubclass(Developer, Employee)    


        
