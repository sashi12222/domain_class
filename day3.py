"""_
what is data structure?
-> A data structure is a data organization, management,and storage format that enables
   efficient access and modification.
   
   types of data strucutre:
     -> Primitive data structure:
         -> integer, float ,character , boolean
         
     -> Non-primitive data strucutre:
        ->Linear data structre:
          arrays linkedlist stack queue
        -> Non-linear data structure:
           Graphs Trees
    
    linear data structure:
    -> in  linear data strucutre , data elements are arranged in a linear order where each and every element is attached
    to  its perevious and next adjacent.
    ->In linear data structure, single level is involed.
    -> its implementation is easy in comparision to non- linear  data structure.
    -> in a linear data structre , memory is not utilized in an efficient way. 
    -> Application of linear data structre are mainly in application software development.
    
    Non-linear data structure:
     -> in non linear data structure , data elements are attached in hierarchically manner.
     -> whereas in non-linear data structure, multiple levels are invlolved
     -> while its implementation is complex in comparsion to linear data structure.
     
     -> while in a non-linear data structure , mmeroy is utilizied in an efficient way.
     -> application of non-linear data structure are in AI and image processsing


   what is stack?
   -> a stack is linear data strucutre that follows the principle of last in first out. this means the last
   elements inserted inside the stack is the first element to be removed.
   
   
   there are some basic opeartions that can be performed on stack:
   stack ADT (abstract data type):
     -> push: add an element to the top of stack
     ->pop:remove an elements from the top of stack
     ->peek: get the value of the top element without removing it
     ->isEmpty: check if the stack is empty
     ->isFull: check if the stack is full
     
     what is abstract data type?
     -> an abstract data type is a mathematical model for data types where a data type is defined by its behavior
      example:
      #driver code
        class Stack:
          def __init__(self,size):
             self.size=size
              self.stack=[None for i in range(size)]
              sel.top=-1
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
            for in range(self.top,-1,-1):
              if i==self.top:
                 print(self.stack[i],"top")
                else:
                  print(self.stack[i])  
         #user code
         size=int(input("Enter the size of stack:"))
         s=Stack(size)
         
         while True:
           os.system("cls")
           print("*** Stack operations ***")
           s.display()
            print("1.Push")
            print("2.Pop")
            print("isEmpty")
            print("isFull")
            print("5.Peek")
            print("6.Exit")
            choice=int(input("Enter your choice:"))         
           if op==1:
             value=int(input("Enter teh value to be pushed:"))
              s.push(value)
           elif op==2:
               print("Popped value is:",s.pop())
           elfi op==3:
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
              break
            else:
              print("Invalid choice")
    """