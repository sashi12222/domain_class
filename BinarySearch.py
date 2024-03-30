    
"""

Binary search:
=> binary search is a very fast and efficient searching technique.
=>bineary serach is used for searching an element in a sorted array.
=> binary search works on the principle of divide and conquer.
-> in this method , to search an element you can compare it with the present element in the middle of the array.
if it matches , the search is successful otherwise the list is divided into two halves:
=> one from 0th element to the middle element which is the center element
-> another from the middle element to the last element.

    """
    
x=[2.8,9,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
print(*x)
val= int(input("Enter the value to be searched:"))
l=0
h=len(x)-1
mid=(l+h)//2
flag=False
if x[mid]==val:
    print("Value found at index:",mid)
    flag=True
else:
     while x[mid]!=val and l<h:
         if x[mid]<val:
             l=l+1
            
         else:
             h=h-1
         mid=(l+h)//2
         if x[mid]==val:
                print("Value found at index:",mid)
                flag=True
                break
if flag==False:
    print("Value not found")