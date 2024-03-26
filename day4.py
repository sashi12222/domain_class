"""

what is queue?
=> a queue is linear data structure that stores items in a first in first out manner. this means the first element. With a queue the least recently added element is removed first.


it is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket.


Bsic operations of queue:

A queue is an object that allows the following operations:

=> enqueue: add an element to the end of the queue
-> dequeue: remove an element from the front of the queue
-> is_empty: check if the queue is empty
->is_full: check if the queue is full
=> peek: get the value of the front of the queue without removing it

Application of queue:
-> cpu scheduling , disk scheduling
-> when data is transferred asynchronously between two processes. the queue is used for synchronization. for example: IO Buffers, pipes, file IO, etc.
-> handling of interrupts in real-time systems.
-> call center phone system use queues to hold people calling them in order.



types of queue:
=> there are four types of queue:
  -> simple queue
  -> circular queue
  -> priority queue
  -> double-ended queue
  
  #simple queue:
  #Enqueue operation:
    -> it adds an item to the queue. if the queue is full, then it is said to be an overflow condition.
    
    #dequeue operation:
    => it removes an item from the queue. the items are popped in the same order in which they are pushed. if the queue is empty, then it is said to be an underflow condition.
    
    #drawback of simple queue:
    -> the drawback of the simple queue is that the queue is full even though there are empty spaces in the queue. this is because the queue is full when the rear is at the end of the queue.
    """