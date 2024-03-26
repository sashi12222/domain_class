"""_
what is class:
in python every thing is an object . to create objects we required some model or plan or blue print ,which is nothing but class.
we can write a class to represent properties and actions of objecty.
properties can be represented by variable
actions can be represented by methods.

how to define a class?
we can define a class by using keyword.
 syntax
 class  classname:
         '''documenttation string'''
         variables: instance variable , static and local variables 
         methods: instance methods,static methods, class methods
         constructer:default constructerzero argument , parameterized constructer


constructor:
 ->constructer is a special method in python.
 ->the name of the constructershould be__init_(self)
 -> constructer will be executed automatically at the time of object creation.
 -> the main purpose of constructer is to declare and initialize instance variables.
 -> per object constructer will be executed only once.
 -> constructer can tyake at least one argument.
 -> constructer is optional and if we are not providing any constructer then python will provide default constructer
 example:
 def_init_(self,name,rollno,marks):
     self.name=name
     self.rollno=rollno
     self.marks=marks

self variables:
-> self is the defaultvariable which is always pointing to current object(like this keyword in java)
-> by using self we can access instance variableand instance methodsof object.

note: self shold be first parameter inside cinstructor def_init_(self):
-> self should be first parameter inside  instance methodsdef  of talk(self):

NOTE: contructor will be executed only once per object method wiil be executed no. of time per object


Types of variable:
 there are three Types of variable available
  1.instancevariables(object level variables)
  2. static variables(class level variables)
  3. local variables(method level variables)

instance variable:
 --> If the value of a variable ia varied from object to object, then such type of variables are called instance variable
 --> for every objecta separate copy of instance variable  will be created.
  
  where we can declare instance variables:
  --> inside constructor by using self variable 
--> inside instance methodby using self variable
--> outside of the class by using object reference variable

How to access instance variables:
 We can access instance variables with in the class by using self variable and outside of the class by using object reference.

 static variabls:
 -->if the value of a variable is not varied from object to object , such type of variables we have to declare with in the class directly but outside of methods.
 Such types of variables are called Static variables.
 -->for total class only one copy of static variable will be  created znd shared by all objects of that class.
 -->we can access static variables either by class name or by object reference.
 but recommended to use class name.

 instance variable vs Static variable:
 --> In the case  of instance variables for every object a seprarte copy  will be created .
 -->BUt  in the case of static variables for total class only one copy will be created and shared by  every object of that class.

Various places to declare static variables:
1) In general we can declare by using class name
2) Inside instance method by using class name 
3) Inside classmethod by using either class name or cls variable
4) Inside static method by using class name

    """