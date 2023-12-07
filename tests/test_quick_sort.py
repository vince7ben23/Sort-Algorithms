import random
from src.sort.quick_sort import QuickSortRecursiveLomuto, QuickSortRecursiveHoare, QuickSortIterativeLomuto

def test_quick_sort_recursive():
    sample = random.sample(range(1,11), 10)
    QuickSortRecursiveLomuto.quick_sort(sample, 0, len(sample)-1)
    assert sample == list(range(1, 11))

def test_quick_sort_iterative():
    sample = random.sample(range(1,11), 10)
    QuickSortIterativeLomuto.quick_sort(sample, 0, len(sample)-1)
    assert sample == list(range(1, 11))

def test_quick_sort_recursive_hoare():
    sample = random.sample(range(1,11), 10)
    QuickSortRecursiveHoare.quick_sort(sample, 0, len(sample)-1)
    assert sample == list(range(1, 11))