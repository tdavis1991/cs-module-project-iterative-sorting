# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i+1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j
        arr[i], arr[cur_index] = arr[cur_index], arr[i]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)# length of the array

    for i in range(n - 1): #iterate through the length of the array
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr



'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr


import unittest
import random
# from iterative_sorting import *

class IterativeSortingTest(unittest.TestCase):
    def test_selection_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [0, 1, 2, 3, 4, 5]
        arr4 = random.sample(range(200), 50)

        self.assertEqual(selection_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(selection_sort(arr2), [])
        self.assertEqual(selection_sort(arr3), [0,1,2,3,4,5])
        self.assertEqual(selection_sort(arr4), sorted(arr4))

    def test_bubble_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [0, 1, 2, 3, 4, 5]
        arr4 = random.sample(range(200), 50)

        self.assertEqual(bubble_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(bubble_sort(arr2), [])
        self.assertEqual(bubble_sort(arr3), [0,1,2,3,4,5])
        self.assertEqual(bubble_sort(arr4), sorted(arr4))

    # Uncomment this test to test your count_sort implementation
    # def test_counting_sort(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [1, 5, -2, 4, 3]
    #     arr4 = random.sample(range(200), 50)

    #     self.assertEqual(counting_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
    #     self.assertEqual(counting_sort(arr2), [])
    #     self.assertEqual(counting_sort(arr3), "Error, negative numbers not allowed in Count Sort")
    #     self.assertEqual(counting_sort(arr4), sorted(arr4))


if __name__ == '__main__':
    unittest.main()