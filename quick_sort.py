class QuickSortRecursive:
    """quick sort
    
    steps: pivot(partition), sort, then divid
    """    
    @classmethod
    def quick_sort(cls, arr: list, left: int, right: int) -> None:
        """qiuck sort with a recursive approach

        Args:
            arr (list): _description_
            left (int): _description_
            right (int): _description_
        """        
        if left < right:
            pivot = cls._partition(arr, left, right)
            cls.quick_sort(arr, left, pivot-1)
            cls.quick_sort(arr, pivot+1, right)

    @staticmethod
    def _partition(arr: list, left: int, right: int) -> int:
        """_summary_

        refer to https://rust-algo.club/sorting/quicksort/

        Args:
            arr (list): _description_
            left (int): _description_
            right (int): _description_

        Returns:
            int : the final index of the pivot
        """
        # set the rightmost as pivot
        ind_final_pivot = left

        for ind in range(left, right+1):
            if arr[ind] < arr[right]:
                arr[ind], arr[ind_final_pivot] = arr[ind_final_pivot], arr[ind]
                ind_final_pivot += 1
        arr[right], arr[ind_final_pivot] = arr[ind_final_pivot], arr[right]
        return ind_final_pivot

class QuickSortIterative:
    """quick sort with a iterative appoach
    """
    @classmethod
    def quick_sort(cls, arr: list, left: int, right: int) -> None:
        """quick sort with a iterative appoach
        implement with a stack to store the left and the right of partitions 

        Args:
            arr (list): _description_
            left (int): _description_
            right (int): _description_
        """        
        stack = []
        # put the right first, then left 
        stack.append(right)
        stack.append(left)
        

        while stack:
            start = stack.pop()
            end = stack.pop()

            pivot_ind = cls._partition(arr, start, end)
            
            if pivot_ind > start+1: 
                stack.append(pivot_ind-1)
                stack.append(start)
            if pivot_ind < end-1:
                stack.append(end)
                stack.append(pivot_ind+1)

    @staticmethod
    def _partition(arr: list, left: int, right: int) -> int:
        """_summary_

        refer to https://rust-algo.club/sorting/quicksort/

        Args:
            arr (list): _description_
            left (int): _description_
            right (int): _description_

        Returns:
            int : the final index of the pivot
        """
        ind_final_pivot = left

        for ind in range(left, right+1):
            if arr[ind] < arr[right]:
                arr[ind], arr[ind_final_pivot] = arr[ind_final_pivot], arr[ind]
                ind_final_pivot += 1
        
        arr[ind_final_pivot], arr[right] = arr[right], arr[ind_final_pivot]
        
        return ind_final_pivot

