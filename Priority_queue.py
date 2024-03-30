import os,time

class priorityqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def isFull(self):
        if (self.rear+1)%self.size==self.front:
            return True
        else:
            return False
    def isEmpty(self):
        if self.front==self.rear==-1:
            return True
        else:
            return False
    def enqueue(self,val):
        if self.isFull():
            print("Queue is full")
        else:
            if self.front==self.rear==-1:
                self.front+=1
                self.rear+=1
                self.queue[self.rear]=val
            else:
                self.rear=(self.rear+1)%self.size
                self.queue[self.rear]=val
    def dequeue(self):
        i=self.front
        max=0
        while i!=self.rear:
            if self.queue[i]>self.queue[max]:
                max=i
            i=(i+1)%self.size
            if self.queue[max]<self.queue[self.rear]:
                x=self.queue[self.rear]
                self.rear-=1
            elif self.rear==self.front:
                x=self.queue[self.rear]
                self.front=self.rear=-1
            else:
                x=self.queue[max]
                i=max
                for i in range(max,self.rear+1):
                  if i+1<=self.rear:
                    self.queue[i]=self.queue[i+1]
                self.rear-=1
            return x
    def peek(self):
        return self.queue[self.front]
    def display(self):
        if self.front==self.rear==-1:
            print()
        else:
            for i in range(self.front,self.rear+1):
                if i==self.front==self.rear:
                    print(self.queue[i],"==> front,rear")
                elif i==self.front:
                    print(self.queue[i],"==> front")
                elif i==self.rear:
                    print("|")
                    print(self.queue[i],"==> rear")
                else:  
                    print("|")     
                    print(self.queue[i])
                    
print("***Priority Queue Implementation***")
size=int(input("Enter the size of the queue: "))
q=priorityqueue(size)
while True:
    os.system("clear")
    print("***Circular Queue Operations***")
    print()
    q.display()
    print()
    print("1.insert\n2.delete\n3.peek\n4.isempty\n5.isfull\n6.exit")
    op=int(input("Enter your choice: "))
    if op==1:
        if q.isFull():
            print("Queue is full")
            time.sleep(1)
        else:       
            val=int(input("Enter the element to insert: "))
            q.enqueue(val)
    elif op==2:
        if q.isEmpty():
            print("Queue is empty")
            time.sleep(1)
        else:
            print("Deleted element is: ",q.dequeue())
            time.sleep(1)
    elif op==3:
        if q.isEmpty():
            print("Queue is empty")
            time.sleep(1)
        else:   
            print("Front element is: ",q.peek())
            time.sleep(1)
    elif op==4:
        if q.isEmpty():
            print("Queue is empty")
            time.sleep(1)
        else:
            print("Queue is not empty")
            time.sleep(1)
    elif op==5:
        if q.isFull():
            print("Queue is full")
            time.sleep(1)
        else:
            print("Queue is not full")
            time.sleep(1)
    elif op==6:
        print("Exiting....")
        time.sleep(1)
        break      
        