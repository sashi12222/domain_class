import sys
import os
#driver code
class Stack:
          def __init__(self,size):
            self.size=size
            self.stack=[None for i in range(size)]
            self.top=-1
          def isFull(self):
            if self.size==self.top+1:
              return True
            else:
              return False
              
          def isEmpty(self):
            if self.top==-1:
              return True
            else:
              return False
              
          def push(self,value):
            if self.isFull():
               print("Stack is full")
            else:
                self.top+=1
                self.stack[self.top]=value
          
          def pop (self):
            if self.isEmpty():
               print("Stack is empty")
            else:
               value=self.stack[self.top]
               self.top-=1
               return value
          def peek(self):
            if self.isEmpty():
               print("Stack is empty")
            else:
               return self.stack[self.top]
          def display(self):
            for i in range(self.top,-1,-1):
              if i==self.top:
                 print(self.stack[i],"top")
              else:
                  print(self.stack[i])  
         #user code
size=int(input("Enter the size of stack:"))
s=Stack(size)
         
while True:
           os.system("clear")
           print("*** Stack operations ***")
           s.display()
           print("1.Push")
           print("2.Pop")
           print("3.isEmpty")
           print("4.isFull")
           print("5.Peek")
           print("6.Exit")
           op=int(input("Enter your choice:"))         
           if op==1:
            value=int(input("Enter teh value to be pushed:"))
            s.push(value)
           elif op==2:
            print("Popped value is:",s.pop())
           elif op==3:
            if s.isEmpty():
                print("Stack is empty")
            else:
                print("Stack is not empty")
           elif op==4:
            if s.isFull():
                print("Stack is full")
            else:
                print("Stack is not full")
           elif op==5:
            print("Top element is:",s.peek())
           elif op==6:
                sys.exit()
           else:
                print("Invalid choice")