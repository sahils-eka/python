def partition(arr, first, last):
    pivot = arr[last]

    # pointer to greater value
    i = first - 1

    for j in range(first, last):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[last] = arr[last], arr[i+1]
    return i+1


def quicksort(arr, first, last):
    if first < last:
        pe = partition(arr, first, last)

        # left part
        quicksort(arr, first, pe-1)

        # right part
        quicksort(arr, pe+1, last)


data = [7, 2, 5, 1, 12, 9, 0]
print(f"Unsorted data is: {data}")

size = len(data)-1

quicksort(data, 0, size)
print(f"Sorted data= {data}")
