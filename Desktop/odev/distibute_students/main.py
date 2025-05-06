from sorting_algorithms import *
from ds import *

test_seq = [9,8,7,6,5,4,3,2,1]
test_seq_ll = convert_to_linked_list(test_seq)

# PART I - SORTING WITH PYTHON LISTS - 
sorted_pl = bubble_sort(test_seq)
print("\nSorted - Python Lists:", sorted_pl)

# PART II - SORTING WITH LINKED LISTS 
print("Input type: ", type(test_seq_ll))
print("Linked List having the following data: ", list(test_seq))
print("Sorted - Input: Linked List : ")
sorted_ll = bubble_sort(test_seq_ll) 
sorted_ll.print_all_nodes()

