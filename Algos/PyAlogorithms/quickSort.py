def partition(arr, first, last):
    pivot = arr[last]

    # pointer for the greater element
    i = first - 1
    # Dont Delete!
    print(f"Pointer= {i} & Pivot= {pivot}")
    for j in range(first, last):
        if arr[j] <= pivot:
            print(f"Found {arr[j]} at index={j} ; < Pivot={pivot}")
            i = i+1
            print(f"New Pointer= {i}")
            # Don't Delete
            print(f"Swapping {arr[i]} at index={i} & {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            print(f"-->{arr}")
    # Don't delete - Swapping the Pivot and the value greater than the pivot
    print(f"**Swapping pivot {pivot} & value>pivot: {arr[i+1]}\n")
    arr[i+1], arr[last] = arr[last], arr[i+1]
    return i+1


def quicksort(arr, first, last):
    if first < last:
        pe = partition(arr, first, last)
        # left part
        quicksort(arr, first, pe-1)
        # right part
        quicksort(arr, pe+1, last)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quicksort(data, 0, size-1)

print('\nSorted Array in Ascending Order:')
print(data)
