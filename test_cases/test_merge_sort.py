import random
from src.sort.merge_sort import MergeSortRecursive, MergeSortIterative, MergeSortIterativeWithStack

def test_merge_sort_recursive():
    sample = random.sample(range(1,11), 10)
    MergeSortRecursive.merge_sort(sample, 0, len(sample)-1)
    assert sample == list(range(1, 11))

def test_merge_sort_iterative():
    sample = random.sample(range(1,11), 10)
    MergeSortIterative.merge_sort(sample)
    assert sample == list(range(1, 11))

def test_merge_sort_iterative_with_stack():
    sample = random.sample(range(1,11), 10)
    MergeSortIterativeWithStack.merge_sort(sample, 0, len(sample)-1)
    assert sample == list(range(1, 11))

 