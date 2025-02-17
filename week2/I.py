def binary_search_first(arr, key):
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            first = mid
            high = mid - 1  # Move left to find first occurrence
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return first


def binary_search_last(arr, key):
    low, high = 0, len(arr) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            last = mid
            low = mid + 1  # Move right to find last occurrence
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return last


def find_key_occurrences(arr, key):
    first_index = binary_search_first(arr, key)
    if first_index == -1:
        return "Key not present"

    last_index = binary_search_last(arr, key)
    count = last_index - first_index + 1
    return f"{key} - {count}"


# Reading input
T = int(input())  # Number of test cases
for _ in range(T):
    n = int(input())  # Size of array
    arr = list(map(int, input().split()))  # Sorted array
    key = int(input())  # Key to be searched
    print(find_key_occurrences(arr, key))
