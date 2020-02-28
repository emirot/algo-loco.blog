

def quick_sort(arr):
    
    if len(arr) < 2:
        return arr

    z = (len(arr)-1)  // 2
    pivot = arr[z]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    
    arr = [-4, 3, 2, 1, 10, 9]
    z = quick_sort(arr)
    arr = [100, -4,20, 3, -30, 2, 8, 1, 10, 9]
    z = quick_sort(arr)
    print("z:", z)
