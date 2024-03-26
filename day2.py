"""
How to access static variables:
> inside constructor : by using either self or claassname
-> inside instance method: by using either self or classname
-> inside class method: by using either cls variable or classname
-> inside static mehtod: by using calassname
-> From outside of class: by using either object reference or classname

example:
 class Test:
  x=99
  def __init__(self):
    print("Constructor:",Test.x)
    def m1(self):
    print("Instance method:",self.x)
    def m2(cls):
    print("Class method:",cls.x)
    def m3():
    print("Static method:",Test.x)
    
    t=Test()
    t.m1() # Test.m1() invalid
    Test.m2()
    Test.m3()
    print(Test.x)
    
    NOTE:
    If we change the value of static varaible by using either self or object reference variable, then the value of static variable won't be changed, 
    a new instance variable with that name will be added to that object.
    Example 1:
    
    class Test:
     a=10 
     def m1(self):
       self.a=888
    t1=Test()
    t1.m1()
    print(Test.a)
    print(t1.a)
    
    Example 2:
    
    calss Test:
    x=10
    def __init__(self):
      self.y=20
      t1=Test()
      t2=Test()
      print("t1:",t1.x,t1.y)
      print("t2:",t2.x,t2.y)
      t1.x=888
      t1.y=999
      print("t1:",t1.x,t1.y)
      print("t2:",t2.x,t2.y)
      
      how to delete static varaible of a class:
      
      
      
      
      
      
      
      
      Local variable:
        -> sometimes to meet temporary requirements of programmer, we can declare variables inside a method directly, such type of variables are called local variables.   
        -> Local variables will be created at the time of method execution and destroyed once method execution completes.
        ->.local variables of a method cannot be accessed from outside of method.
        Example1:                                                
         class Test:
         def m1(self):
         a=1000
         print(a)
         def m2(self):
         b=2000
         print(b)
         t=Test()
         t.m1()
         t.m2()
         
         Example 2:
          
          class Test:
         def m1(self):
         a=1000
         print(a)
         def m2(self):
         b=2000
         print(a) #invalid
         print(b)
         t=Test()
         t.m1()
         t.m2()
         
         Note: name 'a' is not defined
         
         Types of method:
          -> inside python 3 types of methods are allowed
            1. Instance method
            2. Class method
            3. Static method
            
            Instance method:
              __> inside method implementation if we are using instance variables then such type of methods are called instance methods.
              -> inside instance method implementation, we have to pass self variable.
                   def m1(self):
                -> by using self variable inside method, we can able to access instance variables.
                -> within the class we can call instance method by using self variable and from outside of the cals  we can call by using  object reference.
                
                
                #driver code
                
                class Student:
                  def __init__(self,rno,name,marks):
                    self.rno=rno
                    self.name=name
                    self.marks=marks
                   def stu_details(self):
                     print("Student roll number:",self.rno)
                     print("Student name:",self.name)
                     self.grade()
                    def grade(self):
                    if self.marks<=100:
                      if self.marks>80 and self.marks<=100:
                        print("Student grade is A")
                      elif self.marks>60 and self.marks<=80:
                        print("Student grade is B")
                      elif self.marks>40 and self.marks<=60:
                        print("Student grade is C")
                      else:
                        print("Student grade is D")
                    else:
                        print("Invalid marks")
            
            #user code
            rno=int(input("Enter student roll number:"))
            name=input("Enter student name:")
            marks=int(input("Enter student marks:"))
            s=Student(rno,name,marks)
            s.stu_details()
            
            Class Methods:
             -> inside the method implementation if we are using only class variables (static variables) then such type of methods we should declare as class methods.
             -> we have to declare class method explicitly by using @classmethod decorator.
             -> for class method we should provide cls variable at the time of declaration.
             -> we can call class method by using classname or object reference.
             
             Example:
            class Animals:
                legs=4
                @classmethod
                def walk(cls,name):
                    print("{} walks with {} legs".format(name,cls.legs))
            Animals.walk("Dog")
            Animals.walk("Cat")
            
            
            Example2:
             class Test:
              count=0
              def __init__(self):
               Test.count+=1
               @classmethod
               def getNoOfObjects(cls):
                print("The number of objects created:",cls.count)
            t1=Test()
            t2=Test()
            t3=Test()
            Test()
            t4=Test()
            t5=Test()
            Test.noOfObjects()
            
            NOTE:
            Which object doesn't have reference to the object, such type of objects are eligible for garbage collection.
            
            purpose of garbage collector:
              -> every object created in heap area should be destroyed by garbage collector.
              -> every object occupy some memory , garbage collector remove of memory which is occupied by object doesn't have reference. 
              
              
              Static method:
              -> In general these method are general utility methods.
              -> Inside these method we won't use any instance or class variables.
              -> Here we won't provide self or cls arguments at the time of declaration.
              -> we can declare static method explicitly by using @staticmethod decorator.
              -> we can call static method by using classname or object reference.
              
              Example:
                class TwinkleMath:
                  @staticmethod
                   def add(x,y):
                    print("The sum of {} and {} is {}".format(x,y,x+y))
                   @staticmethod
                   def product(x,y):
                    print("The product of {} and {} is {}".format(x,y,x*y))
                 @staticmethod
                 def average(x,y):
                  print("The average of {} and {} is {}".format(x,y,(x+y)/2))
                TwinkleMath.add(10,20)
                TwinkleMath.product(10,20)
                TwinkleMath.average(10,20)
                
                Note: 
                In general we can use only instance and static method . Inside static method we can't use instance variables or 
                we can access class level variables by using class name.
                
               
    """