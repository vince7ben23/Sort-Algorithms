import random
from timeit import timeit

from sort.merge_sort import MergeSortRecursive, MergeSortIterative, MergeSortIterativeWithStack
from sort.quick_sort import QuickSortRecursive, QuickSortIterative, QuickSortRecursiveHoare

ELEMENT_IN_ARRAY = 1000000
NUM_TO_RUN = 1

def test_recursive_merge_sort(seq=range(0, ELEMENT_IN_ARRAY), num=ELEMENT_IN_ARRAY):
    """_summary_

    Args:
        seq (_type_, optional): _description_. Defaults to range(0, 100).
        num (int, optional): _description_. Defaults to 100.
    """  
    sample = random.sample(seq, num)
    MergeSortRecursive.merge_sort(sample, 0, len(sample)-1)

def test_iterative_merge_sort_with_queue(seq=range(0, ELEMENT_IN_ARRAY), num=ELEMENT_IN_ARRAY):
    """_summary_

    Args:
        seq (_type_, optional): _description_. Defaults to range(0, 100).
        num (int, optional): _description_. Defaults to 100.
    """ 
    sample = random.sample(seq, num)
    MergeSortIterative.merge_sort(sample)

def test_iterative_merge_sort_with_stack(seq=range(0, ELEMENT_IN_ARRAY), num=ELEMENT_IN_ARRAY):
    """_summary_

    Args:
        seq (_type_, optional): _description_. Defaults to range(0, 100).
        num (int, optional): _description_. Defaults to 100.
    """ 
    sample = random.sample(seq, num)
    MergeSortIterativeWithStack.merge_sort(sample, 0, len(sample)-1)

def test_recursive_quick_sort(seq=range(0, ELEMENT_IN_ARRAY), num=ELEMENT_IN_ARRAY):
    """_summary_

    Args:
        seq (_type_, optional): _description_. Defaults to range(0, 100).
        num (int, optional): _description_. Defaults to 100.
    """    
    sample = random.sample(seq, num)
    QuickSortRecursive.quick_sort(sample, 0, len(sample)-1)

def test_iterative_quick_sort(seq=range(0, ELEMENT_IN_ARRAY), num=ELEMENT_IN_ARRAY):
    """_summary_

    Args:
        seq (_type_, optional): _description_. Defaults to range(0, 100).
        num (int, optional): _description_. Defaults to 100.
    """    
    sample = random.sample(seq, num)
    QuickSortIterative.quick_sort(sample, 0, len(sample)-1)

def test_recursive_quick_sort_hoare(seq=range(0, ELEMENT_IN_ARRAY), num=ELEMENT_IN_ARRAY):
    """_summary_

    Args:
        seq (_type_, optional): _description_. Defaults to range(0, 100).
        num (int, optional): _description_. Defaults to 100.
    """    
    sample = random.sample(seq, num)
    QuickSortRecursiveHoare.quick_sort(sample, 0, len(sample)-1)

if __name__ == "__main__":
    print("recursive_merge_sort:", timeit(test_recursive_merge_sort, number=NUM_TO_RUN))
    print("iterative_merge_sort_with_queue:", timeit(test_iterative_merge_sort_with_queue, number=NUM_TO_RUN))
    print("iterative_merge_sort_with_stack:", timeit(test_iterative_merge_sort_with_stack, number=NUM_TO_RUN))
    print("recursive_quick_sort:", timeit(test_recursive_quick_sort, number=NUM_TO_RUN))
    print("iterative_quick_sort:", timeit(test_iterative_quick_sort, number=NUM_TO_RUN))
    print("recursive_quick_sort_hoare:", timeit(test_recursive_quick_sort_hoare, number=NUM_TO_RUN))

