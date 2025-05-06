import unittest
from sorting_algorithms import *

class TestSorting(unittest.TestCase):
    l1 = [9,8,7,6,5,4,3,2,1]
    linked_list1 = convert_to_linked_list(l1)

    def test_bubble_sort_list(self):
        self.assertEqual(bubble_sort(self.l1), [1,2,3,4,5,6,7,8,9])

    def test_bubble_sort_linked_list(self):
         self.assertEqual(list(bubble_sort(self.linked_list1)), [1,2,3,4,5,6,7,8,9])

if __name__ == "__main__":
    unittest.main()

    