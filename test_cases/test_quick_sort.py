import random
from src.sort.quick_sort import QuickSortIterative, QuickSortRecursive

def test_quick_sort_recursive():
    sample = random.sample(range(1,11), 10)
    QuickSortRecursive.quick_sort(sample, 0, len(sample)-1)
    assert sample == list(range(1, 11))

def test_quick_sort_iterative():
    sample = random.sample(range(1,11), 10)
    QuickSortIterative.quick_sort(sample, 0, len(sample)-1)
    assert sample == list(range(1, 11))