x=[8,3,2,7,5,4,1,6,9,10,12,11]
val=int(input("Enter the value to search: "))
flag=False

for i in range(len(x)):
    if x[i]==val:
        print("Element found at position:",i)
        flag=True
        break
if flag==False:
    print("Element not found")
    
    """_
    Searching Techniques:
    => searching is the process of finding a given value position in a list of values.
    -> it decides whether the given value is present in the list or not.
    => it is the algorithmic process of finding a particular item in a collection of items.
    
    -> it can be done on internal data structures like arrays, linked lists, trees, graphs, or on external data structures like files.
    
    Searching techniques:
    -> linear search
    -> Binary search
    
    Linear search or sequential search:
    -> sequential search is  also called linear search.
    -> this method can be performed on both sorted and unsorted lists.
    -> sequential search start at beginning of the list and check each element until the desired element is found or the end of the list is reached.
    
    -> sequental search compares the element with all the other elements in the list. if the element is matched,it returns the index of the element,else it returns -1.
    
    x=[1,2,3,4,5,6,7,8,9,10]
    print(*x)
    val=int(input("Enter the value to search: "))
    try:
        print("Element found at position:",x.index(val))
    except valueError:
        print("Element not found")
        
    """