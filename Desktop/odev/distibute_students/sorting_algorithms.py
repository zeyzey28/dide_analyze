from ds import *

def bubble_sort(theSeq):
    if isinstance(theSeq, list):
        n = len(theSeq)
        for i in range(n - 1):
            for j in range(n - (i + 1)):
                if theSeq[j] > theSeq[j + 1]:
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
        return theSeq
    
    elif isinstance(theSeq, LinkedList):
        n = theSeq.num_items
        for i in range(n - 1):
            current = theSeq.head
            for j in range(n - (i + 1)):
                if current.data > current.next.data:
                    # Swap data values
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp
                current = current.next
        return theSeq
    else:
        raise TypeError("Input must be either a list or LinkedList")


