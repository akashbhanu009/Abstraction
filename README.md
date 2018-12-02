# Abstraction
Simple code to know about abstraction
here the concept was that
the abstraction class eg:- class Hello (ABC), which was inherite from the 'abc'-Abstract Base Class module, using " from abc import * "
and the abstaract method was declare by the decorator= 

@abstractmethod
def m1(self): pass

we can't create any object of abstraction class with abstraction method. You can mentioned in the child class after inherite the abstract class. If ypu are on;y inherite the parent class in the child class and not describe or mention in the abstract method then that child class was also behave as a abstract class with there abstract method and constructor, So, you should to be declare it in the child class, then only make a reference variable of child class and access the action of the abstract method
