def find_sequence(arr):
    n = len(arr)

    # Fix k and use two-pointer approach for i, j
    for k in range(2, n):
        i, j = 0, k - 1

        while i < j:
            if arr[i] + arr[j] == arr[k]:
                return f"{i+1}, {j+1}, {k+1}"  # 1-based indexing

            elif arr[i] + arr[j] < arr[k]:
                i += 1
            else:
                j -= 1

    return "No sequence found"


# Reading input
T = int(input())  # Number of test cases
for _ in range(T):
    n = int(input())  # Size of array
    arr = list(map(int, input().split()))  # Sorted array
    print(find_sequence(arr))
