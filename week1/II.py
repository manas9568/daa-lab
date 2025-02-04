def search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return "present"
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return "not present"


n = int(input("Enter the size of the array: "))
arr = sorted([int(input(f"Enter element {i+1}: ")) for i in range(n)])
key = int(input("Enter the key to search: "))

print(search(arr, key))
