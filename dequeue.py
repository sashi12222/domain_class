"""

Deque Data structure:
=> Deque is a double-ended queue, which means that you can add and remove elements from both ends of the queue.
=>Deque or double ended queue  is a type of queue in which insertion and deletion of elements can be performed from either front or rear.

=> thus, it does not follow the FIFO rule.

Types of Deque:
-> Input Restricted Deque:
     In this deque, input is restricted at a single end but allows deletion at both ends.
-> Output Restricted Deque:
        In this deque, output is restricted at a single end but allows insertion at both ends.
        
    Applicatoins of deque data structure:
    _=> In undo operations on software.
     -> To store history in browsers.
     => For implementing both stacks and queues.
    """
import os,time
class deque:
    def  __init__(self,size):
            self.size=size
            self.queue=[None for i in range(size)]
            self.front=self.rear=-1
    def isFull(self):
        if (self.rear+1)%self.size==self.front:
            return True
        else:
            return False
    def enqueueFront(self,val):
        if self.front==self.rear==-1:
            self.front+=1
            self.rear+=1
            self.queue[self.front]=val
        elif self.front==0:
            self.front=self.size-1
            self.queue[self.front]=val
        else:
            self.front-=1
            self.queue[self.front]=val
    def enqueueRear(self,val):
        if self.front==self.rear==-1:
            self.front+=1
            self.rear+=1
            self.queue[self.rear]=val
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=val
    def dequeueRear(self):
        if self.rear==self.front:
            x=self.queue[self.rear]
            self.front=self.rear=-1
        else:
            x=self.queue[self.rear]
            self.rear-=1
            return x
    def dequeueFront(self):
        if self.rear==self.front:
            x=self.queue[self.front]
            self.front=self.rear=-1
        else:
            x=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return x
    def isEmpty(self):
        if self.front==self.rear==-1:
            return True
        else:
            return False    
    def display(self):
     if self.front==self.rear==-1:
        print()
     else:
        i=self.front
        while i!=self.rear:
            if  i==self.front:
                print(self.queue[i],"<== front")
            else:
                print("|")
                print(self.queue[i])
                i=(i+1)%self.size
        if self.front==self.rear:
            print("|")
            print(self.queue[i],"<== front,rear")
        else:
            print("|")
            print(self.queue[i],"<== rear")
print("****Deque Implementation****")
size=int(input("Enter the size of the deque: "))
q=deque(size)

while True:
    os.system("clear")
    print("***Operations on Deque***")
    print()
    q.display()
    print() 
    print("1. Enqueue Front\n 2. Enqueue Rear\n")
    op=int(input("Enter your choice: "))
    if op==1:
        if q.isFull():
            print("Queue is full")
            time.sleep(1)
        else:
            val=int(input("Enter the element to insert: "))
            q.enqueueFront(val)
    elif op==2:
        if q.isFull():
            print("Queue is full")
            time.sleep(1)
        else:
            val=int(input("Enter the element to insert: "))
            q.enqueueRear(val)    
    