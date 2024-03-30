import os,time
class circular:
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
        if self.isEmpty():
            print("Queue is empty")
        else:
            if self.front==self.rear:
                x=self.queue[self.front]
                self.front=self.rear=-1
                return x
            else:
                x=self.queue[self.front]
                self.front=(self.front+1)%self.size
                return x
            
    def peek(self):     
        return self.queue[self.front]
    
    def display(self):
     if self.front == self.rear == -1:
        print()
     else:
        i = self.front
        while i != self.rear:
            if i == self.front:
                print(self.queue[i], "==> front")
            else:
                print("|")
                print(self.queue[i])
            i = (i + 1) % self.size
        if self.front == self.rear:
            print(self.queue[i], "==> front,rear")
        else:
            print("|")
            print(self.queue[i], "==> rear")
            
print("***Circular Queue Implementation***")
size=int(input("Enter the size of the queue: "))
q=circular(size)
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