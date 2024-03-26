import os

class queue:
    #creation of queue
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = -1
        self.rear = -1

    #isEmpty
    def is_empty(self):
        if self.front==self.rear==-1:
            return True
        else:
            return False

    #isFull
    def is_full(self):
        if self.size==self.rear+1:
            return True
        else:
            return False
        
    #enqueue
    def enqueue(self,value):
         if self.is_full():
             return "Queue is full"
         elif self.front==self.rear==-1:
             self.front+=1
             self.rear+=1
             self.queue[self.rear]=value
         
    #dequeue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        elif self.front==self.rear:
            x=self.queue[self.front]
            self.front=self.rear=-1
            return x
        else:
            x=self.queue[self.front]
            self.front+=1
            return x

    def peek(self):
        return self.queue[self.front]

    def display(self):
        if self.front == -1:
            print("No elements in the Queue")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")

print("***Queue Operations***")
size = int(input("Enter the size of the Queue: "))
q=queue(size)

while True:
    os.system("clear")
    print("1.insert\n2.delete\n3.peek\n4.is_empty\n5.is_full\n6.exit\n")
    op=int(input("Enter your option: "))
    if op==1:
     if q.is_full():
         print("Queue is full")
     else:
         val=int(input("Enter the value to insert: "))
         q.enqueue(val)
    elif op==2:
        if q.is_empty():
            print("Queue is empty")
        else:
            print("Deleted element is:",q.dequeue())
    elif op==3:
        if q.is_empty():
            print("Queue is empty")
        else:
            print("Front element is:",q.queue[q.front])
    elif op==4:
        if q.is_empty():
            print("Queue is empty")
        else:
            print("Queue is not empty")
    elif op==5:
        if q.is_full():
            print("Queue is full")
        else:
            print("Queue is not full")
    elif op==6:
        break
    else:
        print("Invalid option")
    
    q.display()