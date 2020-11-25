def binarySearch(arr, low, high, x):
    while(low<=high):
        mid = low + (high-low)//2

        if arr[mid]==x:
            return mid+1
        elif arr[mid] <x:
            low = mid+1
        else:
            high = mid-1
    return -1


arr = [2,3,5,6,15,25,40,66,99,120,126]
x = 66

result = binarySearch(arr, 0, len(arr)-1, x)

if result !=-1:
    print("Element found at position %d" % result)
else:
    print("Element is not present in the array")