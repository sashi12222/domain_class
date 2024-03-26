import os,time

class queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def isEmpty(self):
        if self.front==self.rear==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.rear+1==self.size:
            return True
        else:
            return False
    def enqueue(self,val):
        if self.front==self.rear==-1:
            self.front+=1
            self.rear+=1
            self.queue[self.rear]=val
        else:
            self.rear+=1
            self.queue[self.rear]=val
    def dequeue(self):
        if self.front==self.rear:
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
        
        
print("***Queue Implementation***")
size=int(input("Enter the size of the queue: "))
q=queue(size)
while True:
    os.system("clear")
    print("***Queue Operations***")
    print()
    q.display()
    print()
    print("1.insert\n2.delete\n3.peek\n4.isEmpty\n5.isFull\n6.exit")
    op=int(input("Enter your choice: "))
    if op==1:
        if q.isFull():
            print("Insertion is not possible,Queue is full")
            time.sleep(1)
        else:
            val=int(input("Enter the value to insert: "))
            q.enqueue(val)
    elif op==2:
        if q.isEmpty():
            print("Queue is empty")
            time.sleep(1)
        else:
            print("Deleted value is: ",q.dequeue())
            time.sleep(1)
    elif op==3:
        if q.isEmpty():
            print("Queue is empty")
            time.sleep(1)
        else:
            print("Peek value is: ",q.peek())
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
        break
    else:
        print("Invalid choice")
        time.sleep(1)
    
          
      
    