from  random import randint


class QuickSortRecursiveLomuto:
    """quick sort with Lomuto partition
    
    steps: pivot(partition), sort, then divid
    """    
    @classmethod
    def quick_sort(cls, arr: list, left: int, right: int) -> None:
        """qiuck sort with a recursive approach

        Args:
            arr (list): array to be sorted
            left (int): start point of sorting range
            right (int): end point of sorting range
        """        
        if left < right:
            pivot = cls._lomuto_partition(arr, left, right)
            cls.quick_sort(arr, left, pivot-1)
            cls.quick_sort(arr, pivot+1, right)

    @staticmethod
    def _lomuto_partition(arr: list, left: int, right: int) -> int:
        """Lomuto's partition

        refer to https://rust-algo.club/sorting/quicksort/

        Args:
            arr (list): array to be sorted
            left (int): start point of sorting range
            right (int): end point of sorting range

        Returns:
            int : the returned index of the pivot
        """
        return_pivot_index = left
        # optimization tips: randomly pick a pivot, then put it to the righmost side
        m = randint(left, right)
        arr[right], arr[m] = arr[m], arr[right]

        for ind in range(left, right+1):
            # use the rightmost element as pivot
            if arr[ind] < arr[right]:
                arr[ind], arr[return_pivot_index] = arr[return_pivot_index], arr[ind]
                return_pivot_index += 1
        
        # set the pivot index to the correct position 
        arr[right], arr[return_pivot_index] = arr[return_pivot_index], arr[right]
        return return_pivot_index

class QuickSortIterativeLomuto:
    """quick sort with a iterative appoach
    """
    @classmethod
    def quick_sort(cls, arr: list, left: int, right: int) -> None:
        """quick sort with a iterative appoach
        implement with a stack to store the left and the right of partitions 

        Args:
            arr (list): array to be sorted
            left (int): start point of sorting range
            right (int): end point of sorting range
        """        
        stack = []
        # put the right first, then left 
        stack.append(right)
        stack.append(left)
        

        while stack:
            start = stack.pop()
            end = stack.pop()

            pivot_ind = cls._lomuto_partition(arr, start, end)
            
            if pivot_ind > start+1: 
                stack.append(pivot_ind-1)
                stack.append(start)
            if pivot_ind < end-1:
                stack.append(end)
                stack.append(pivot_ind+1)

    @staticmethod
    def _lomuto_partition(arr: list, left: int, right: int) -> int:
        ind_final_pivot = left
        
        # optimization tips: randomly pick a pivot, then put it to the righmost side
        m = randint(left, right)
        arr[right], arr[m] = arr[m], arr[right]

        for ind in range(left, right+1):
            if arr[ind] < arr[right]:
                arr[ind], arr[ind_final_pivot] = arr[ind_final_pivot], arr[ind]
                ind_final_pivot += 1
        
        arr[ind_final_pivot], arr[right] = arr[right], arr[ind_final_pivot]
        
        return ind_final_pivot

class QuickSortRecursiveHoare:
    """quick sort with Hoare partition
    
    steps: pivot(partition), sort, then divid
    """    
    @classmethod
    def quick_sort(cls, arr: list, left: int, right: int) -> None:
        """qiuck sort with a recursive approach

        Args:
            arr (list): array to be sorted
            left (int): start point of sorting range
            right (int): end point of sorting range
        """        
        if left < right:
            pivot = cls._hoare_partition(arr, left, right)
            cls.quick_sort(arr, left, pivot)  # note Hoare should include pivot 
            cls.quick_sort(arr, pivot+1, right)

    @staticmethod
    def _hoare_partition(arr: list, left: int, right: int) -> int:
        # optimization tips: pick the pivot randomly 
        # m = (left + right) // 2
        m = randint(left, right)
        pivot = arr[m]

        l_ptr = left
        r_ptr = right

        while True:
            while arr[l_ptr] < pivot: l_ptr += 1
            while arr[r_ptr] > pivot: r_ptr -= 1
            
            if l_ptr >= r_ptr: return r_ptr
            
            arr[l_ptr], arr[r_ptr] = arr[r_ptr], arr[l_ptr]
            l_ptr += 1
            r_ptr -= 1
