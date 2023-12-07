import random
from timeit import timeit

from sort.merge_sort import MergeSortRecursive, MergeSortIterative, MergeSortIterativeWithStack
from sort.quick_sort import QuickSortRecursiveLomuto, QuickSortIterativeLomuto, QuickSortRecursiveHoare


ELEMENT_IN_ARRAY = 1000000
NUM_TO_RUN = 1
SAMPLE = random.sample(range(1, ELEMENT_IN_ARRAY+1), ELEMENT_IN_ARRAY)
# SAMPLE = [10 for _ in range(ELEMENT_IN_ARRAY)] # deplicated elements

def test_recursive_merge_sort():
    MergeSortRecursive.merge_sort(SAMPLE, 0, len(SAMPLE)-1)

def test_iterative_merge_sort_with_queue():
    MergeSortIterative.merge_sort(SAMPLE)

def test_iterative_merge_sort_with_stack():
    MergeSortIterativeWithStack.merge_sort(SAMPLE, 0, len(SAMPLE)-1)

def test_recursive_quick_sort_lomuto():  
    QuickSortRecursiveLomuto.quick_sort(SAMPLE, 0, len(SAMPLE)-1)

def test_iterative_quick_sort_lomuto():
    QuickSortIterativeLomuto.quick_sort(SAMPLE, 0, len(SAMPLE)-1)

def test_recursive_quick_sort_hoare(seq=range(0, ELEMENT_IN_ARRAY), num=ELEMENT_IN_ARRAY): 
    QuickSortRecursiveHoare.quick_sort(SAMPLE, 0, len(SAMPLE)-1)

if __name__ == "__main__":
    print("recursive_merge_sort:", timeit(test_recursive_merge_sort, number=NUM_TO_RUN))
    print("iterative_merge_sort_with_queue:", timeit(test_iterative_merge_sort_with_queue, number=NUM_TO_RUN))
    print("iterative_merge_sort_with_stack:", timeit(test_iterative_merge_sort_with_stack, number=NUM_TO_RUN))
    print("recursive_quick_sort_lomuto:", timeit(test_recursive_quick_sort_lomuto, number=NUM_TO_RUN))
    print("iterative_quick_sort_lomuto:", timeit(test_iterative_quick_sort_lomuto, number=NUM_TO_RUN))
    print("recursive_quick_sort_hoare:", timeit(test_recursive_quick_sort_hoare, number=NUM_TO_RUN))

